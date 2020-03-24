from WhatsAppManifest import ADB, Automator
from WhatsAppManifest.automator.whatsapp import Conversation

# Note: We need the AdbServer class (even without using SSH) so that Automator can open the internal connection.
with ADB(use_ssh=False) as AdbServer:
    automator = Automator(adb_server=AdbServer, adb_host="127.0.0.1", adb_port=5037)

    for device in automator.list_devices(state=None):

        conversation = Conversation(device=device)

        phone = "+0011987654321"
        jid = conversation.phone_str_to_jid(phone=phone)
        created = conversation.chat_exists(jid=jid)

        if created:
            created = conversation.create_chat(phone_number=phone)

        if created:
            conversation.send_message(
                jid=jid,
                message="Hello World!",
                re_open=True,
                wait_send_complete=True
            )
