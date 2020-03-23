from time import sleep

import adbutils
from ppadb.device import Device as AdbDevice

from WhatsAppManifest.consts import _PACKAGE_NAME_, _PACKAGE_VERSION_, _PACKAGE_VERSION_SUPPORT_
from WhatsAppManifest.exception import UnsupportedPackageVersion, PackageNotInstalled
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.adb.ui_automator_remote import UIAutomatorRemote
from WhatsAppManifest.exception import NeverStartedActivity


class Device(WhatsAppManifest):
    """
    Class responsible for facilitating the administration of instances
    of android devices via Android Debug Bridge
    """

    _adb_device: AdbDevice = None
    _adb_utils: adbutils.AdbDevice = None
    _automator = None

    @property
    def adb_device(self) -> AdbDevice:
        """
        :return: Bridge between ADB and device.
        :rtype: AdbDevice
        """
        return self._adb_device

    @property
    def ui_automator(self) -> UIAutomatorRemote:
        """
        :return: UI Automator Instance
        :rtype: UIAutomatorDevice
        todo: Crashing problems were encountered with UI Automator.
        """
        raise NotImplementedError(
            "This function is not yet available due to problems with remote connection to the device.")
        self.logger.debug("Starting UI Automator")
        from WhatsAppManifest.adb.adb import ADB

        server = self.automator._adb_server

        assert isinstance(server, ADB)

        return UIAutomatorRemote(device=self, adb=server)

    @property
    def ui_automator2(self) -> UIAutomatorRemote:

        raise NotImplementedError(
            "This function is not yet available due to problems with remote connection to the device.")

        from WhatsAppManifest.adb.adb import ADB

        server = self.automator._adb_server

        assert isinstance(server, ADB)

        return UIAutomatorRemote(device=self, adb=server)

    @property
    def netcfg(self) -> str:
        return self.adb_device.shell("netcfg")

    @property
    def wlan0(self) -> str:
        return self.adb_device.shell("ip addr show wlan0")

    @property
    def ip_route(self) -> str:
        return self.adb_device.shell("ip route")

    @property
    def adb_utils(self) -> adbutils.AdbDevice:

        if self._adb_utils is None:
            self.logger.debug("Starting ADB utility tools")
            adb = adbutils.AdbClient(host=self.automator.adb_host, port=self.automator.adb_port)
            self._adb_utils = adb.device(self.serial)

        return self._adb_utils

    @property
    def automator(self):
        """
        Return of the Automator module to this device
        """
        return self._automator

    def __init__(self, adb_device: AdbDevice, automator):
        self._adb_device = adb_device
        self._automator = automator

        self.build_logger(type(self).__name__)

        # Check if exploited APK is installed on android device
        self.package_installed()
        # Checks whether exploited APK matches package version
        self.package_version_validate()
        # Checks if the version of the android device is compatible with the package
        self.checkup_phone_version()
        # Checks whether the SDK level is compatible with the package
        self.checkup_sdk_level()

    def checkup_phone_version(self):
        """
        Method to check if andorid version is compatible with the package
        :raises UnsupportedAndroidVersion
        """
        from WhatsAppManifest.consts import _ANDROID_VERSION_, _ANDROID_VERSION_SUPPORT_
        from WhatsAppManifest.automator.android import AndroidPhone
        from WhatsAppManifest.exception import UnsupportedAndroidVersion

        version = AndroidPhone(self).phone_version

        if not _ANDROID_VERSION_(version):
            raise UnsupportedAndroidVersion(
                f"Version {version} is not supported by this package, "
                f"consider switching to one of these: {', '.join(_ANDROID_VERSION_SUPPORT_)}")

    def checkup_sdk_level(self):
        """
        Method to check if the SDK level is compatible with the package
        :raises UnsupportedSDKLevel
        """

        from WhatsAppManifest.consts import _SDK_LEVEL_, _SDK_LEVEL_SUPPORT_
        from WhatsAppManifest.automator.android import AndroidPhone
        from WhatsAppManifest.exception import UnsupportedSDKLevel

        version = AndroidPhone(self).sdk_version
        if not _SDK_LEVEL_(version):
            raise UnsupportedSDKLevel(
                f"SDK {version} is not supported by this package, consider switching to one of these: {', '.join(_SDK_LEVEL_SUPPORT_)}")

    def package_installed(self):
        """
        Checks whether the APK is installed on the device
        :raises PackageNotInstalled
        """
        if not self.adb_device.is_installed(_PACKAGE_NAME_):
            raise PackageNotInstalled("The package is not installed on the device.")

    def package_version_validate(self):
        """
        Checks if the APK version is compatible with the package
        :raises UnsupportedPackageVersion
        """
        version = self.adb_device.get_package_version_name(_PACKAGE_NAME_)

        if not _PACKAGE_VERSION_(version):
            raise UnsupportedPackageVersion(
                f"The {version} version of the package is not supported, consider switching to one of these: {', '.join(_PACKAGE_VERSION_SUPPORT_)}")

    @property
    def genymotion_instance_name(self) -> str:
        """
        :return: Genymotion instance name
        :rtype: str
        """
        return self.product_model

    @property
    def product_model(self) -> str:
        return self.adb_device.get_properties().get("ro.product.model", "")

    @property
    def serial(self) -> str:
        return self.adb_device.serial

    @property
    def current_app(self) -> dict:
        return self.adb_utils.current_app()

    def is_current_activity(self,activity):
        return self.current_app.get("activity") == activity

    def wait_activity(self, activity: list, interval: float = 1.5, retries: int = 3):
        self.logger.debug(f"Waiting for activity {activity}")
        retry = 0

        if isinstance(activity,str):
            activity = [activity]

        while not self.current_app.get("activity") in activity:
            retry += 1

            if retry >= retries:
                raise NeverStartedActivity(f"Couldn't start activity {activity}."
                                           f"Current activity is: {self.current_app}")

            sleep(interval)

        return True

    def send_keyevent(self, keyevent: int, repeats: int = 1):
        self.logger.info(f"Sending event \"{keyevent}\" {repeats} time(s)")

        for repeat in range(repeats):
            self.adb_utils.keyevent(keyevent)
