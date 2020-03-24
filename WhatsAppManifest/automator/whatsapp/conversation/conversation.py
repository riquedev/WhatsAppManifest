import os
from time import sleep
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.consts import _PACKAGE_NAME_
from WhatsAppManifest.adb.device import Device
from WhatsAppManifest.manifest.android import AndroidKeyEvents
from WhatsAppManifest.automator.whatsapp.database import WhatsAppDatabaseMSGStore
from WhatsAppManifest.automator.whatsapp.utils import re_open_package
from WhatsAppManifest.manifest.android.activity import Activities
from WhatsAppManifest.manifest.whatsapp.contact_picker import ContactPicker
from WhatsAppManifest.manifest.whatsapp.api_send import APISend


class Conversation(WhatsAppManifest):
    _device: Device = None
    _msgstore: WhatsAppDatabaseMSGStore = None

    def __init__(self, device: Device):
        self.build_logger(type(self).__name__)
        self._device = device
        self._msgstore = WhatsAppDatabaseMSGStore(device=device)

    def send_message(self, jid: str, message: str, re_open: bool = True, wait_send_complete: bool = False):
        """
        Responsible method for sending text
        :param jid:
        :type jid:
        :param message:
        :type message:
        :param re_open:
        :type re_open:
        :param wait_send_complete:
        :type wait_send_complete:
        :return:
        :rtype:
        """
        if re_open:
            re_open_package(device=self._device, package=_PACKAGE_NAME_)

        picker = ContactPicker()

        # Command constructor
        command = picker.build_send_message(jid, message)

        self.logger.info(f"Opening conversation with contact {jid}")
        command_output = self._device.adb_device.shell(command)
        self.logger.debug(f"{command_output}")

        # We need to wait for the conversation to enter
        self._device.wait_activity(activity=Activities.WhatsAppConversation)

        self.logger.info(f"Pressing the \"ENTER\" key")
        self._device.send_keyevent(AndroidKeyEvents.ENTER)

        if wait_send_complete:
            self.logger.info(f"Waiting confirmation")

            while not self._msgstore.chat_last_message_has_sent(jid):
                sleep(0.2)
                self.logger.info(f"The message has not yet been sent")

    def create_chat(self, phone_number) -> bool:
        """
        Method responsible for creating a chat (using the API) from a phone number, this is necessary for the contact to start appearing in the Contact Picker
        :param phone_number:
        :type phone_number:
        :return: Chat created
        :rtype: bool
        """

        """
            Create chat via api command constructor
        """

        api_send = APISend()
        command = api_send.build_apo_send(phone_number)

        self._device.adb_device.shell(command)

        # Wait activity open
        return self._device.wait_activity(activity=Activities.WhatsAppConversation, throw_exception=False)

    def send_media(self, jid: str, file_path: str, re_open: bool = True, wait_send_complete: bool = False):
        """
        Responsible method for sending media
        :param jid:
        :type jid:
        :param file_path:
        :type file_path:
        :param re_open:
        :type re_open:
        :param wait_send_complete:
        :type wait_send_complete:
        :return:
        :rtype:
        """
        success = False
        file_name = os.path.basename(file_path)

        if re_open:
            re_open_package(device=self._device, package=_PACKAGE_NAME_)

        self._device.adb_device.push(file_path, f"/data/local/{file_name}")

        # Send media command build
        picker = ContactPicker()
        command = picker.build_send_media(jid, file_name)
        self.logger.info(f"Sending media to contact {jid}")

        command_output = self._device.adb_device.shell(command)
        self.logger.debug(f"{command_output}")

        # We can get the activity for selecting the contact or viewing the media
        self._device.wait_activity(activity=[
            Activities.WhatsAppContactPicker,
            Activities.WhatsAppGalleryPickerMediaPreview
        ])

        if self._device.is_current_activity(Activities.WhatsAppContactPicker):

            self._device.send_keyevent(AndroidKeyEvents.TAB, repeats=3)
            self._device.send_keyevent(AndroidKeyEvents.ENTER, repeats=1)
            if self._device.is_current_activity(Activities.WhatsAppConversation):

                if wait_send_complete:
                    self.logger.info(f"Waiting confirmation")

                    while not self._msgstore.chat_last_message_has_sent(jid):
                        sleep(0.2)
                        self.logger.info(f"The message has not yet been sent")

                success = True
            else:
                success = False

        elif self._device.is_current_activity(Activities.WhatsAppGalleryPickerMediaPreview):
            self._device.send_keyevent(AndroidKeyEvents.TAB, repeats=6)
            self._device.send_keyevent(AndroidKeyEvents.ENTER, repeats=1)

            if self._device.is_current_activity(Activities.WhatsAppConversation):

                if wait_send_complete:
                    self.logger.info(f"Waiting confirmation")

                    while not self._msgstore.chat_last_message_has_sent(jid):
                        sleep(0.2)
                        self.logger.info(f"The message has not yet been sent")

                success = True

        return success
