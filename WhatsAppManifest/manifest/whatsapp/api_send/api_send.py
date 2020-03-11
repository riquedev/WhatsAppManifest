from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.android.action import AndroidActionView
from WhatsAppManifest.manifest.whatsapp.sys.flags import ActivityFlags, IntentFlags


class APISend(WhatsAppManifest):
    """
    Manifest for using the WhatsApp Web API, to open a new chat on the phone (without risk of bugs on the screen)
    """
    ACTION = (AndroidActionView,)

    def __init__(self):
        self.build_logger(type(self).__name__)

    def build_apo_send(self, phone):
        self.logger.debug("Command for opening contact via browser successfully built!")
        return self._build_am_start(
            {
                ActivityFlags.WAIT_COMPLETE_LAUNCH: "",
                IntentFlags.ACTION: AndroidActionView,
                IntentFlags.DATA_URI: f"https://api.whatsapp.com/send?phone={phone}"
            },
            app_distinct=True
        )
