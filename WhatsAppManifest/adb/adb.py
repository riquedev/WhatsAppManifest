from ppadb.client import Client as AdbClient
from ppadb.device import Device as AdbDevice
from sshtunnel import SSHTunnelForwarder
import sshtunnel
from WhatsAppManifest.adb.base import WhatsAppManifest


class ADB(WhatsAppManifest):
    """
    Class for controlling Android Debug Bridge, it aims to facilitate the
    administration of connection options with devices.
    todo: Check if local connections are working normally.
    """

    _ssh_tunnel: SSHTunnelForwarder = None
    _use_ssh: bool = False
    _ssh_ip: str = ""
    _ssh_port: int = 22
    _ssh_username: str = "root"
    _ssh_password: str = ""
    _remote_bind_ip: str = "127.0.0.1"
    _remote_bind_port: int = 5037
    _adb_client: AdbClient = None
    _adb_device: AdbDevice = None

    def __init__(self, use_ssh: bool = False, ssh_ip: str = "", ssh_port=22, ssh_username="root", ssh_password=None,
                 remote_bind_ip="127.0.0.1", remote_bind_port=5037):

        self.build_logger(type(self).__name__)

        self._use_ssh = use_ssh
        self._ssh_ip = ssh_ip
        self._ssh_port = ssh_port
        self._ssh_username = ssh_username
        self._ssh_password = ssh_password
        self._remote_bind_ip = remote_bind_ip
        self._remote_bind_port = remote_bind_port

    @property
    def ssh_tunnel(self) -> SSHTunnelForwarder:
        """
        Get SSH Tunnel instance
        :return:
        :rtype:
        """
        if self._ssh_tunnel is None and self._use_ssh:
            self.logger.debug(f"Starting SSH Tunnel {self._ssh_ip}:{self._ssh_port}")
            self.logger.debug(f"Username: {self._ssh_username}")
            self.logger.debug(f"Password: {''.join('*' for x in self._ssh_password)}")

            self._ssh_tunnel = sshtunnel.open_tunnel(
                (self._ssh_ip, self._ssh_port),
                ssh_username=self._ssh_username,
                ssh_password=self._ssh_password,
                remote_bind_address=(self._remote_bind_ip, self._remote_bind_port),
            )

        return self._ssh_tunnel

    @property
    def use_ssh(self) -> bool:
        # Do we need to make use of SSH connection?
        return self._use_ssh

    def start_adb_client(self, host: str = "127.0.0.1", port: int = 5037):
        """
        Start adb client with package
        :param host:
        :type host:
        :param port:
        :type port:
        :return:
        :rtype:
        """

        self.logger.debug(f"Connecting to the ADB Server {host}:{port}")

        self._adb_client = AdbClient(
            host=host,
            port=port
        )

        self.logger.debug(f"Successfully connected to the ADB Server!")

    @property
    def adb_client(self) -> AdbClient:
        """
        Get ADB Terminal Client
        :return:
        :rtype:
        """
        return self._adb_client

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if self._use_ssh:
            self.logger.debug("Stopping SSH Tunnel")
            self.ssh_tunnel.stop()
            self.logger.debug("Closing SSH Tunnel")
            self.ssh_tunnel.close()
