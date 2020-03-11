from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseWA(WhatsAppDatabase):
    """
    WhatsApp WA Database
    """
    _database = Path.wa
