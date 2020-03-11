from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseStatusRanking(WhatsAppDatabase):
    """
    WhatsApp Status Ranking Database
    """
    _database = Path.statusranking


