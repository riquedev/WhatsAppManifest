"""
Data types used on Android and whatsapp
"""


class TextPlain:

    def __str__(self):
        return "text/plain"


class AnyImage:

    def __str__(self):
        return "image/*"


class AndroidVndContact:
    def __str__(self):
        return "vnd.android.cursor.dir/contact"
