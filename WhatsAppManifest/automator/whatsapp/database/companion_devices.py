from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseCompanionDevices(WhatsAppDatabase):
    """
    WhatsApp Companion Devices Database
    """
    _database = Path.companion_devices


