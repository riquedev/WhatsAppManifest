import atexit, uiautomator2, sshtunnel
from WhatsAppManifest.adb.adb import ADB
from uiautomator import Device as UIAutomatorDevice

class UIAutomatorRemote:
    _adb: ADB = None
    _tunnel: sshtunnel.SSHTunnelForwarder = None
    _device = None
    _ui_automator: UIAutomatorDevice = None

    def __init__(self, device, adb: ADB):
        self._adb = adb
        self._device = device
        host, port = device.serial.split(":")
        atexit.register(self.close)

        self._tunnel = sshtunnel.open_tunnel(
            self._adb.ssh_tunnel.ssh_host,
            self._adb.ssh_tunnel.ssh_port,
            ssh_username=self._adb.ssh_tunnel.ssh_username,
            ssh_password=self._adb.ssh_tunnel.ssh_password,
            remote_bind_address=(host, int(port))
        )

        self._tunnel.start()
        self._ui_automator = UIAutomatorDevice(
            device.serial,
            adb_server_host="127.0.0.1",
            adb_server_port=self._tunnel.local_bind_port
        )

    def close(self):
        if self._tunnel.is_active or self._tunnel.is_alive or self._tunnel.tunnel_is_up:
            self._tunnel.stop()

    @property
    def device(self) -> UIAutomatorDevice:
        return self._ui_automator
