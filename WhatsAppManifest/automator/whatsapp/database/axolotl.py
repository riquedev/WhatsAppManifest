from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseAxolotl(WhatsAppDatabase):
    """
    WhatsApp Axolotl database
    """
    _database = Path.axolotl


