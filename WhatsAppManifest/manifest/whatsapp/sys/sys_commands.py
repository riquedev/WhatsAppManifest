from WhatsAppManifest.decorators import classproperty
from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.manifest.android.keyevents import KeyEventsTuple, KeyEvents


class SysCommands:
    """
    Shortcuts to direct system commands to WhatsApp
    """

    @classproperty
    def pm_kill(self) -> str:
        """
        Process kill
        :return: Command string
        :rtype: str
        """
        return f"pmkill {_PACKAGE_NAME_}"

    @classproperty
    def force_stop(self) -> str:
        """
        Force process stop
        :return: Command string
        :rtype: str
        """
        return f"am force-stop  {_PACKAGE_NAME_}"

    @classmethod
    def input_text(cls, text: str) -> str:
        """
        Send text to application
        :param text:
        :type text:
        :return:
        :rtype:
        """
        return f"input text '{text}'"

    @classmethod
    def input_keyevent(cls, code: KeyEventsTuple = KeyEvents.UNKNOWN) -> str:
        return f"input keyevent {code}"

    @classmethod
    def sleep(cls, seconds: int) -> str:
        return f"sleep {seconds}"
