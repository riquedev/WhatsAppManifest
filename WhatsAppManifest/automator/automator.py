from typing import Iterator
from ppadb.client import Client as AdbClient
from WhatsAppManifest.adb import ADB, WhatsAppManifest, Device
from WhatsAppManifest.consts import _ADB_VERSION_, _ADB_VERSIONS_SUPPORTED_
from WhatsAppManifest.exception import UnsupportedADB


class Automator(WhatsAppManifest):
    """
    Automate all Android (and APK) Functions
    """

    _adb_server: ADB = None
    _adb_host: str = ""
    _adb_port: int = 5037

    def __init__(self, adb_server: ADB, adb_host="127.0.0.1", adb_port=""):

        # Create Logger using logging lib
        self.build_logger(type(self).__name__)

        # ADB Setup
        self._adb_server = adb_server
        self._adb_host = adb_host
        self._adb_port = adb_port

        # Check ADB Lifestate
        self.checkup_adb()

    def checkup_adb(self):
        """
        Checks whether the ADB version is compatible with the automator
        :raises: UnsupportedADB
        """
        if not _ADB_VERSION_(self.adb_version):
            raise UnsupportedADB(
                f"The {self.adb_version} version of ADB is not yet supported, consider switching to one of these: {', '.join(_ADB_VERSIONS_SUPPORTED_)}")

    @property
    def adb_host(self) -> str:
        return self._adb_host

    @property
    def adb_port(self) -> int:
        return self._adb_port

    @property
    def adb_version(self) -> int:
        return self.adb_client.version()

    def get_device(self, serial: str) -> Device:
        """
        :param serial: Device identificator
        :type serial: str
        :return: Device instance
        :rtype: Device
        """

        return Device(self.adb_client.device(serial), automator=self)

    def list_devices(self, state=None) -> Iterator[Device]:
        """

        :param state: State of device list
        :type state: Any
        :return: Generator of Device
        :rtype: Iterator[Device]
        """
        for device in self.adb_client.devices(state):
            yield Device(device, automator=self)

    @property
    def adb_server(self) -> ADB:
        """
        Returns the ADB server and starts it, if necessary

        :return: ADB Server Instance
        :rtype: ADB
        """

        if self._adb_server.use_ssh and (
                not self._adb_server.ssh_tunnel.is_alive or not self._adb_server.ssh_tunnel.is_active):
            # Starting SSH Tunnel
            self.logger.info("Trying to start SSH Tunnel")
            self._adb_server.ssh_tunnel.start()
            self.logger.info(f"SSH Tunnel started successfully!")
            self.logger.info(f"{self._adb_server.ssh_tunnel.tunnel_bindings}")

        return self._adb_server

    @property
    def adb_client(self) -> AdbClient:
        """
        Returns ADB Client and starts it, if necessary
        :return: ADB Client
        :rtype: AdbClient
        """

        if not self._adb_server.adb_client:

            # We need the port to be really an integer
            self._adb_port = int(
                self._adb_port if not self.adb_server.use_ssh else self.adb_server.ssh_tunnel.local_bind_port)

            self._adb_server.start_adb_client(
                host=self._adb_host,
                port=self.adb_port
            )

        return self._adb_server.adb_client
