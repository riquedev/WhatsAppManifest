import os
from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.decorators import classpathproperty as classproperty


class Path:
    """
    WhatsApp paths
    """

    @classproperty
    def package_data(self) -> str:
        return os.path.join("data", "data", _PACKAGE_NAME_)

    @classproperty
    def databases(self) -> str:
        return os.path.join(Path.package_data, "databases")

    @classproperty
    def msgstore(self) -> str:
        return os.path.join(Path.databases, "msgstore.db")

    @classproperty
    def axolotl(self) -> str:
        return os.path.join(Path.databases, "axolotl.db")

    @classproperty
    def chatsettings(self) -> str:
        return os.path.join(Path.databases, "chatsettings.db")

    @classproperty
    def companion_devices(self) -> str:
        return os.path.join(Path.databases, "companion_devices.db")

    @classproperty
    def emojidictionary(self) -> str:
        return os.path.join(Path.databases, "emojidictionary.db")

    @classproperty
    def location(self) -> str:
        return os.path.join(Path.databases, "location.db")

    @classproperty
    def media(self) -> str:
        return os.path.join(Path.databases, "media.db")

    @classproperty
    def msgstore(self) -> str:
        return os.path.join(Path.databases, "msgstore.db")

    @classproperty
    def payments(self) -> str:
        return os.path.join(Path.databases, "payments.db")

    @classproperty
    def statusranking(self) -> str:
        return os.path.join(Path.databases, "statusranking.db")

    @classproperty
    def stickers(self) -> str:
        return os.path.join(Path.databases, "stickers.db")

    @classproperty
    def wa(self) -> str:
        return os.path.join(Path.databases, "wa.db")
