from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.whatsapp.sys.flags import IntentFlags
from WhatsAppManifest.manifest.android.action import AndroidActionSend
from WhatsAppManifest.manifest.whatsapp.types import TextPlain
from WhatsAppManifest.manifest.whatsapp.extra import Jid, AndroidExtraText


class ContactPicker(WhatsAppManifest):
    ACTION = (AndroidActionSend,)
    CATEGORY = ()
    TYPE = (TextPlain,)
    EXTRA = (Jid, AndroidExtraText)

    def __init__(self):
        self.build_logger(type(self).__name__)

    @property
    def namespace(self) -> str:
        """
        :return: Identificação da classe em Java.
        :rtype: str
        """
        return f"{_PACKAGE_NAME_}/.ContactPicker"

    def build_send_message(self, jid: str, message: str) -> str:
        self.logger.debug("Building command for change picture")

        return self._build_am_start({
            IntentFlags.COMPONENT: self.namespace,
            IntentFlags.ACTION: AndroidActionSend,
            IntentFlags.MIME_TYPE: TextPlain,
            IntentFlags.EXTRA_STRING_VALUE: [
                {
                    "value": Jid,
                    "extra": f"'{jid}'"
                },
                {
                    "value": AndroidExtraText,
                    "extra": f"'{message}'"
                }
            ]

        })
