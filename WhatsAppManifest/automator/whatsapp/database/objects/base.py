class DatabaseObject(dict):

    @property
    def id(self) -> int:
        return int(self.get("_id", ""))
