from WhatsAppManifest.automator.whatsapp.database.objects.base import DatabaseObject
from datetime import datetime
from typing import Any


class Message(DatabaseObject):

    @property
    def jid(self) -> int:
        return int(self.get("jid_row_id", "-1"))

    @property
    def remote_jid(self) -> str:
        return self.get("key_remote_jid", "")

    @property
    def from_me(self) -> bool:
        return self.get("key_from_me", "") == "1"

    @property
    def key_id(self) -> str:
        return self.get("key_id", "")

    def status_by_code(self, code: str) -> str:
        is_received = (code == "0", code == "5",)
        is_system_message = (code == "6",)
        is_waiting_in_server = (code == "4",)
        is_audio_played = (code == "8", code == "10",)
        is_seen = (code == "13" or code == "12",)

        if any(is_received):
            return "received"

        elif any(is_system_message):
            return "system_message"

        elif any(is_waiting_in_server):
            return "waiting_in_server"

        elif any(is_audio_played):
            return "played"

        elif any(is_seen):
            return "seen"

        else:
            return "unknown"

    @property
    def status_code(self) -> str:
        return self.get("status", "")

    @property
    def status(self) -> str:
        return self.status_by_code(self.status_code)

    @property
    def needs_push(self) -> bool:
        return self.get("needs_push", "0") == "1"

    @property
    def data(self) -> str:
        return self.get("data", "")

    @property
    def timestamp(self) -> Any:
        timestamp = self.get("timestamp", "")

        if timestamp.strip():
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def media_url(self) -> str:
        return self.get("media_url", "")

    @property
    def media_mime_type(self) -> str:
        return self.get("media_mime_type", "")

    @property
    def media_wa_type(self) -> str:
        return self.get("media_wa_type", "")

    @property
    def media_size(self) -> int:
        return int(self.get("media_size", "0"))

    @property
    def media_name(self) -> str:
        return self.get("media_name", "")

    @property
    def media_caption(self) -> str:
        return self.get("media_caption", "")

    @property
    def media_hash(self) -> str:
        return self.get("media_hash", "")

    @property
    def media_duration(self) -> int:
        return int(self.get("media_duration", "0"))

    @property
    def origin(self) -> str:
        return self.get("origin", "")

    @property
    def latitude(self) -> float:
        return float(self.get("latitude", "0.0"))

    @property
    def longitude(self) -> float:
        return float(self.get("longitude", "0.0"))

    @property
    def thumb_image(self) -> str:
        return self.get("thumb_image", "")

    @property
    def remote_resource(self) -> str:
        return self.get("remote_resource", "")

    @property
    def received_timestamp(self) -> Any:
        timestamp = self.get("received_timestamp", "")

        if timestamp.strip():
            timestamp = int(timestamp) / 1000

            if timestamp < 0:
                return None

            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def send_timestamp(self) -> Any:
        timestamp = self.get("send_timestamp", "")

        if timestamp.strip():
            if timestamp == "-1":
                timestamp = "0"
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def receipt_server_timestamp(self) -> Any:
        timestamp = self.get("receipt_server_timestamp", "")

        if timestamp.strip():
            if timestamp == "-1":
                timestamp = "0"
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def receipt_device_timestamp(self) -> Any:
        timestamp = self.get("receipt_device_timestamp", "")

        if timestamp.strip():
            if timestamp == "-1":
                timestamp = "0"
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def read_device_timestamp(self) -> Any:
        timestamp = self.get("read_device_timestamp", "")

        if timestamp.strip():
            if timestamp == "-1":
                timestamp = "0"
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def played_device_timestamp(self) -> Any:
        timestamp = self.get("played_device_timestamp", "")

        if timestamp.strip():
            if timestamp == "-1":
                timestamp = "0"
            timestamp = int(timestamp) / 1000
            return datetime.fromtimestamp(timestamp)
        else:
            return None

    @property
    def raw_data(self) -> str:
        return self.get("raw_data", "")

    @property
    def recipient_count(self) -> int:
        return int(self.get("recipient_count", "0"))

    @property
    def participant_hash(self) -> str:
        return self.get("participant_hash", "")

    @property
    def starred(self) -> str:
        return self.get("starred", "")

    @property
    def quoted_id(self) -> str:
        return self.get("quoted_row_id", "")

    @property
    def mentioned_jids(self) -> str:
        return self.get("mentioned_jids", "")

    @property
    def multicast_id(self) -> str:
        return self.get("multicast_id", "")

    @property
    def edit_version(self) -> str:
        return self.get("edit_version", "")

    @property
    def media_enc_hash(self) -> str:
        return self.get("media_enc_hash", "")

    @property
    def payment_transaction_id(self) -> str:
        return self.get("payment_transaction_id", "")

    @property
    def forwarded(self) -> bool:
        return self.get("forwarded", "") == ""

    @property
    def preview_type(self) -> str:
        return self.get("preview_type", "")

    @property
    def send_count(self) -> int:
        return int(self.get("send_count", "0"))
