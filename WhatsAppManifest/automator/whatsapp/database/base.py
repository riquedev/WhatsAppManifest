import csv, uuid, tempfile, os
from typing import Iterator
from WhatsAppManifest.adb.device import Device
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.whatsapp.path import Path


class WhatsAppDatabase(WhatsAppManifest):
    """
    Base class for the database
    """

    _device = None
    _data = None
    _database = None
    _uuid = None

    def __init__(self, device: Device):
        self.build_logger(type(self).__name__)

        self.logger.info("Starting WhatsApp Database connection")
        self.logger.info(f"Database: {self._database}")

        self._device = device

        # Unique operation uuid
        self._uuid = str(uuid.uuid4())

    def refresh_data(self):
        return NotImplementedError("Method refresh not implemented")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @property
    def temp_file(self) -> str:
        """
        Returns the temporary file directory for this instance
        :return: Temp file path
        :rtype: str
        """

        return f"/data/local/{self._uuid}.csv"

    def query(self, query) -> Iterator[dict]:
        content = b""
        sintax = f"sqlite3 -header -csv {self._database} \"{query}\"  > {self.temp_file}"

        self.logger.debug(f"Sending to shell: {sintax}")

        self._device.adb_device.shell(sintax)

        for chunk in self._device.adb_utils.sync.iter_content(self.temp_file):
            content += chunk

        # The temporary file will be filled with the answer data
        f = tempfile.TemporaryFile(delete=False)
        f.write(content)
        f.close()

        output = [dict(row) for row in csv.DictReader(open(f.name, "r", encoding="utf-8", errors="ignore"))]

        self.logger.debug(f"Deleting {f.name}")

        # Here we will remove the temporary files on Android and on the computer
        os.remove(f.name)
        self.logger.debug(f"Deleting {self.temp_file}")
        self._device.adb_utils.remove(self.temp_file)
        return output

    def get_all_tables(self) -> Iterator[dict]:
        query = "SELECT * FROM sqlite_master WHERE type='table' ORDER BY name;"
        return self.query(query)

    def get_all_rows(self, table, condition=None) -> Iterator[dict]:
        query = f"SELECT * FROM {table}" if condition is None else f"SELECT * FROM {table} where {condition}"
        return self.query(query)

    @property
    def databases(self) -> list:
        return str(self._device.adb_utils.shell(f"find {Path.databases} -iname *.db")).splitlines()

    @property
    def so_databases(self) -> list:
        return str(self._device.adb_utils.shell(f"find / -iname *.db")).splitlines()
