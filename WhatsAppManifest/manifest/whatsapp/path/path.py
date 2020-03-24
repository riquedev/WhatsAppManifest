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
    def data_media(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join("data", "media", "0", "WhatsApp Business","Media")
        else:
            raise NotImplementedError("The path to the media files of ordinary WhatsApp has not yet been implemented.")

    @classproperty
    def avatars(self) -> str:
        return os.path.join(Path.files, "Avatars")

    @classproperty
    def cache_profile_pictures(self) -> str:
        return os.path.join(Path.cache, "Profile Pictures")

    @classproperty
    def animated_gifs(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media,"WhatsApp Business Animated Gifs")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def audio_files(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Audio")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def documents_files(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Documents")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def images_files(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Images")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def profile_photos(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Profile Photos")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def quick_reply_attachments(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Quick Reply Attachments")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def stickers_files(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Stickers")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def video_files(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Stickers")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def voice_notes(self) -> str:
        if _PACKAGE_NAME_ == "com.whatsapp.w4b":
            return os.path.join(self.data_media, "WhatsApp Business Voice Notes")
        else:
            raise NotImplementedError("This directory has not yet been specified.")

    @classproperty
    def files(self) -> str:
        return os.path.join(Path.package_data, "files")

    @classproperty
    def cache(self) -> str:
        return os.path.join(Path.package_data, "cache")

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
