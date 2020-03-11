from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.android.category import AndroidCategoryDefault
from WhatsAppManifest.manifest.android.action import AndroidAttachData
from WhatsAppManifest.manifest.whatsapp.types import AnyImage
from WhatsAppManifest.manifest.whatsapp.extra import MimeType


class SetProfilePicture(WhatsAppManifest):
    ACTION = (AndroidAttachData,)
    CATEGORY = (AndroidCategoryDefault,)
    TYPE = (AnyImage,)
    EXTRA = (MimeType,)

    def __init__(self):
        self.build_logger(type(self).__name__)

    @property
    def namespace(self) -> str:
        """
        :return: Identificação da classe em Java.
        :rtype: str
        """
        return f"{_PACKAGE_NAME_}/.SetAsProfilePhoto"

    def build_set_profile_picture(self, file_path: str) -> str:
        self.logger.debug("Building command for change picture")

        return self._build_am_start({
            "n": self.namespace,
            "a": self.ACTION[0](),
            "c": self.CATEGORY[0](),
            "d": file_path,
            "t": self.TYPE[0](),
            "e": {
                "value": self.EXTRA[0](),
                "extra": self.TYPE[0]()
            }

        })
