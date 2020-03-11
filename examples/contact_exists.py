from WhatsAppManifest import ADB, Automator
from WhatsAppManifest.automator.android import AndroidContacts

# Note: We need the AdbServer class (even without using SSH) so that Automator can open the internal connection.
with ADB(use_ssh=False) as AdbServer:
    automator = Automator(adb_server=AdbServer, adb_host="127.0.0.1", adb_port=5037)

    for device in automator.list_devices(state=None):
        android_contacts = AndroidContacts(device)
        assert android_contacts.contact_exists("+001198765-4321")
