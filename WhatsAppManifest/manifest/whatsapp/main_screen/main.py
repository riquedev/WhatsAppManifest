from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.adb.base import WhatsAppManifest


class MainScreen(WhatsAppManifest):

    def __init__(self):
        self.build_logger(type(self).__name__)

    @property
    def namespace(self) -> str:
        """
        :return: Identificação da classe em Java.
        :rtype: str
        """
        return f"{_PACKAGE_NAME_}/.Main"

    def build_open_screen(self) -> str:
        self.logger.debug("Building command for opening main screen")

        return self._build_am_start({
            "n": self.namespace
        }, app_distinct=False)
