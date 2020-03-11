from WhatsAppManifest import ADB, Automator

# Note: We need the AdbServer class (even without using SSH) so that Automator can open the internal connection.
with ADB(use_ssh=False) as AdbServer:
    
    automator = Automator(adb_server=AdbServer, adb_host="127.0.0.1", adb_port=5037)

    for device in automator.list_devices(state=None):
        help(device.ui_automator)
