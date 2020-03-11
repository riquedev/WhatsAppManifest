from WhatsAppManifest.automator.whatsapp.database.objects.base import DatabaseObject


class Jid(DatabaseObject):

    @property
    def user(self) -> str:
        return self.get("user", "")

    @property
    def server(self) -> str:
        return self.get("server", "")

    @property
    def agent(self) -> bool:
        return bool(int(self.get("agent", "0")))

    @property
    def device(self) -> bool:
        return bool(int(self.get("device", "0")))

    @property
    def type(self) -> int:
        return int(self.get("type", "-1"))

    @property
    def raw_string(self) -> str:
        return self.get("raw_string", "")
