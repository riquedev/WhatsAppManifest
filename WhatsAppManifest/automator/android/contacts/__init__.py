import re
from typing import Iterator
from WhatsAppManifest.adb import Device
from WhatsAppManifest.automator.android.objects import AndroidContact
from WhatsAppManifest.manifest.android import AndroidKeyEvents
from WhatsAppManifest.adb.base import WhatsAppManifest
from WhatsAppManifest.manifest.whatsapp.sys.flags import IntentFlags
from WhatsAppManifest.manifest.android.action import AndroidActionInsert
from WhatsAppManifest.manifest.whatsapp.types import AndroidVndContact


class AndroidContacts(WhatsAppManifest):
    """
    Object responsible for providing access to the contact data of the Android device
    """

    _device: Device = None

    def __init__(self, device: Device):
        self._device = device
        self.build_logger(type(self).__name__)

    @property
    def device(self) -> Device:
        return self._device

    @property
    def contacts(self) -> Iterator[AndroidContact]:
        """
        :return: Contact list iterator
        :rtype: AndroidContact
        """

        shell_content = self.device.adb_utils.shell("content query --uri content://contacts/phones/")

        for line in str(shell_content).splitlines():

            contact = AndroidContact()

            for key, value, value2 in re.findall(r'([^\s|=]+)=(\s*([a-zA-Z^\s\d|]+)|)', line):
                contact[key] = value

            yield contact

    def get_contact(self, phone: str) -> Iterator[dict]:
        """
        Gets a specific contact from the list
        :param phone: Desired phone number
        :type phone: string
        :return: Iterator of dict
        :rtype: Iterator
        """
        return filter(lambda data: data.get("number", "") == phone, self.contacts)

    def contact_exists(self, phone: str) -> bool:
        """
        Checks if the phone number is not already on the android device
        :param phone: Phone number
        :type phone: string
        :return: Contact exists
        :rtype: bool
        """
        phone = ''.join(filter(str.isdigit, phone))
        return len(list(self.get_contact(phone))) > 0

    def save_contact(self, name, phone) -> bool:
        """

        :param name:
        :type name:
        :param phone:
        :type phone:
        :return:
        :rtype:
        """
        from bs4 import BeautifulSoup

        command = self._build_am_start(
            {
                IntentFlags.ACTION: AndroidActionInsert,
                IntentFlags.MIME_TYPE: AndroidVndContact,
                IntentFlags.EXTRA_STRING_VALUE: [
                    {
                        "value": "name",
                        "extra": f"{name}"
                    },
                    {
                        "value": "phone",
                        "extra": f"{phone}"
                    }
                ]
            },
            app_distinct=False
        )

        self.device.adb_utils.shell(command)

        # The dump is done to try to get the contact sync notification, and thus be able to click to not sync.
        xml = self.device.adb_utils.dump_hierarchy()
        soup = BeautifulSoup(xml)

        for soup in soup.find_all("node", {"resource-id": "com.android.contacts:id/text"}):

            if soup.has_attr("text") and "contacts online" in soup["text"]:
                #  Some devices may already start with the "do not sync" button in focus, so we hit enter.
                self.device.adb_device.input_keyevent(AndroidKeyEvents.ENTER)
                self.device.adb_device.input_keyevent(AndroidKeyEvents.TAB)
                self.device.adb_device.input_keyevent(AndroidKeyEvents.ENTER)

        #  The HOME button is capable of saving the contact, it is worth noting that this is not guaranteed to work correctly
        #  todo: Search for a way to ensure that the contact has been saved or not
        self.device.adb_device.input_keyevent(AndroidKeyEvents.HOME)

        # It is necessary to finish the process, otherwise, when we return,
        # android will try to save the previous contact again.
        self.device.adb_utils.app_stop("com.android.contacts")

        return self.contact_exists(phone)
