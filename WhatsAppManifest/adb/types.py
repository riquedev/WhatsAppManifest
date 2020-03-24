class Log(str):
    text: str

    def __init__(self, content):
        self.text = content

    @property
    def date(self) -> str:
        return self.text[:5]

    @property
    def time(self) -> str:
        return self.text[6:18]

    @property
    def pid(self) -> int:
        return int(self.text[18:].split()[0])

    @property
    def tid(self) -> int:
        return int(self.text[18:].split()[1])

    @property
    def priority(self) -> str:
        return str(self.text[18:].split()[2])

    @property
    def tag(self) -> str:
        return str(self.text[18:].split()[3])[:-1]

    @property
    def message(self) -> str:
        tag = str(self.text[18:].split()[3])
        return self.text[18:].split(sep=tag)[1].lstrip()
