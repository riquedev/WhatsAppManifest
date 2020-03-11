from WhatsAppManifest.tools import APKPureDownload
from apkparser.apk import APK

apk_pure = APKPureDownload()

apk_pure.download_apk("com.whatsapp.w4b", path=".", file_name=None)

help(APK("com.whatsapp.w4b.apk"))
