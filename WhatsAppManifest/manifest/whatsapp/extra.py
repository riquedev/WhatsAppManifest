"""
    Extra methods used in Android and Whatsapp calls
"""


class AndroidExtraText:

    def __str__(self):
        return "android.intent.extra.TEXT"


class SmsBody:

    def __str__(self):
        return "sms_body"


class MimeType:

    def __str__(self):
        return "mimeType"


class Jid:

    def __str__(self):
        return "jid"


class AndroidExtraStream:
    def __str__(self):
        return "android.intent.extra.STREAM"
