from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabasePayments(WhatsAppDatabase):
    """
    WhatsApp Payments Database
    """
    _database = Path.payments


