from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.manifest.android.keyevents import KeyEvents
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.whatsapp.sys import SysCommands
from WhatsAppManifest.manifest.android.category import AndroidCategoryBrowsable, AndroidCategoryDefault
from WhatsAppManifest.manifest.whatsapp.scheme import DataSms, DataSmsTo
from WhatsAppManifest.manifest.android.action import AndroidActionSendTo
from WhatsAppManifest.manifest.whatsapp.types import TextPlain
from WhatsAppManifest.manifest.whatsapp.extra import SmsBody


class Conversation(WhatsAppManifest):
    ACTION = (AndroidActionSendTo,)
    DATA = (DataSms, DataSmsTo,)
    CATEGORY = (AndroidCategoryDefault, AndroidCategoryBrowsable,)
    TYPE = (TextPlain,)
    EXTRA = (SmsBody,)

    def __init__(self):
        self.build_logger(type(self).__name__)

    @property
    def namespace(self) -> str:
        """
        :return: Identificação da classe em Java.
        :rtype: str
        """
        return f"{_PACKAGE_NAME_}/.Conversation"

    def build_contact_sms_to(self, jid: str) -> str:
        """
        Contrução do comando abd para abertura de uma conversa
        :param jid: ID do usuário ou do grupo, ex: 123456789@s.whatsapp.net
        :type jid: str
        :return: Command string
        :rtype: str
        """
        self.logger.debug("Building command for opening contact")

        return self._build_am_start({
            "n": self.namespace,
            "a": self.ACTION[0](),
            "c": self.CATEGORY[0](),
            "d": f"{self.DATA[1]()}:{jid}",
            "e": {
                "value": f"{self.EXTRA[0]()}",
                "extra": f"''"
            }
        })

    def build_sms_to_send_message(self, jid: str, message: str) -> list:
        return [
            self.build_contact_sms_to(jid),
            SysCommands.input_text(message),
            SysCommands.input_keyevent(KeyEvents.TAB),
            SysCommands.input_keyevent(KeyEvents.TAB),
            SysCommands.input_keyevent(KeyEvents.ENTER)
        ]


print(Conversation().build_open_contact("5527997179730@s.whatsapp.net"))
