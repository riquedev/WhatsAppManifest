from WhatsAppManifest.automator.whatsapp.database.objects.base import DatabaseObject
from datetime import datetime
from typing import Any


class Chat(DatabaseObject):

    @property
    def jid_id(self) -> int:
        return int(self.get("jid_row_id", "-1"))

    @property
    def hidden(self) -> bool:
        return bool(int(self.get("hidden", "0")))

    @property
    def subject(self) -> str:
        return self.get("subject", "")

    @property
    def created_timestamp(self) -> Any:
        created_timestamp = self.get("created_timestamp", "")

        if created_timestamp.strip():
            created_timestamp = int(created_timestamp) / 1000
            return datetime.fromtimestamp(created_timestamp)
        else:
            return None

    @property
    def display_message_id(self) -> Any:
        return int(self.get("display_message_row_id", "-1"))

    @property
    def last_message_id(self) -> Any:
        return int(self.get("last_message_row_id", "-1"))

    @property
    def last_read_message_id(self) -> Any:
        return int(self.get("last_read_message_row_id", "-1"))

    @property
    def has_unread_messages(self) -> bool:
        return self.last_read_message_id < self.last_message_id

    @property
    def last_read_receipt_sent_message_id(self) -> int:
        return int(self.get("last_read_receipt_sent_message_row_id","-1"))
