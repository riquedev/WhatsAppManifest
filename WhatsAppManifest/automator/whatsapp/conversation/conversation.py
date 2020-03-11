from time import sleep
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.adb.device import Device
from WhatsAppManifest.manifest.android import AndroidKeyEvents
from WhatsAppManifest.automator.whatsapp.database import WhatsAppDatabaseMSGStore


class Conversation(WhatsAppManifest):
    _device: Device = None
    _msgstore: WhatsAppDatabaseMSGStore = None

    def __init__(self, device: Device):
        self.build_logger(type(self).__name__)
        self._device = device
        self._msgstore = WhatsAppDatabaseMSGStore(device=device)

    def send_message(self, jid: str, message: str, re_open: bool = True, wait_send_complete: bool = False):
        from WhatsAppManifest.manifest.whatsapp.contact_picker import ContactPicker

        if re_open:
            self._device.adb_utils.app_stop(_PACKAGE_NAME_)

        picker = ContactPicker()
        command = picker.build_send_message(jid, message)

        self.logger.info(f"Opening conversation with contact {jid}")
        command_output = self._device.adb_device.shell(command)
        self.logger.debug(f"{command_output}")

        while self._device.adb_utils.current_app().get("activity") != "com.whatsapp.Conversation":
            sleep(1)

        self.logger.info(f"Pressing the \"ENTER\" key")
        self._device.adb_utils.keyevent(AndroidKeyEvents.ENTER)

        if wait_send_complete:

            while True:
                sleep(2)
                message = self._msgstore.last_contact_message(jid)

                if message is not None and message.status in ["seen", "received", "waiting_in_server"]:
                    break

    def create_chat(self, phone_number):
        from WhatsAppManifest.manifest.whatsapp.api_send import APISend

        api_send = APISend()
        command = api_send.build_apo_send(phone_number)

        return self._device.adb_device.shell(command)
