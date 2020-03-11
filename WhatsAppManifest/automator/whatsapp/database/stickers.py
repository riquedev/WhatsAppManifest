from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseStickers(WhatsAppDatabase):
    """
    WhatsApp Stickers Database
    """
    _database = Path.stickers


