from WhatsAppManifest.adb import Device


class AndroidPhone(object):
    """
    Object for android device, responsible for facilitating access to data from Android device
    """
    _device: Device = None

    def __init__(self, device: Device):
        self._device = device

    @property
    def phone_version(self) -> str:
        return self._device.adb_utils.shell("getprop ro.build.version.release")

    @property
    def device(self) -> Device:
        return self._device

    @property
    def sdk_version(self) -> str:
        return self._device.adb_utils.shell("getprop ro.build.version.sdk")
