from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseLocation(WhatsAppDatabase):
    """
    WhatsApp Location Database
    """
    _database = Path.location
