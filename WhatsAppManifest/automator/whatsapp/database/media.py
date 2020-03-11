from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseMedia(WhatsAppDatabase):
    """
    WhatsApp Media Database
    """
    _database = Path.media


