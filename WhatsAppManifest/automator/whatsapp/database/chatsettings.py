from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseChatSettings(WhatsAppDatabase):
    """
    WhatsApp Chatsettings database
    """
    _database = Path.chatsettings


