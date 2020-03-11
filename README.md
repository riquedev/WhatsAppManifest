# WhatsAppManifest

### What is it?
This package is used to provide a python interface to interact with WhatsApp to send, receive messages, configure your profile, among other functions...

This package can perform its functions using the Android Debug Bridge (adb).

### Installation
#### Dependencies

- You will need to install [Android Debug Bridge](https://www.xda-developers.com/install-adb-windows-macos-linux/ "Android Debug Bridge") on your machine
- A rooted phone (you can also use [Genymotion](https://www.genymotion.com/ "Genymotion"))

#### From Source
- Clone the repository
- Use `pip install -r requirements.txt` to install the required packages

#### Usage

##### 1. Import library
```python
from WhatsAppManifest import ADB, Automator
```

##### 2. Start Server
```python
# Local ADB
with ADB(use_ssh=False) as AdbServer:
    automator = Automator(adb_server=AdbServer, adb_host="127.0.0.1", adb_port=5037)

# Remote ADB
with ADB(use_ssh=True,
         ssh_ip="<SSH-IP>",
         ssh_port=22,
         ssh_username="<SSH-USERNAME>",
         ssh_password="<SSH-PASSWORD>",
         remote_bind_ip="127.0.0.1",  # ADB SERVER INTERNAL IP
         remote_bind_port=5037  # ADB SERVER PORT
         ) as AdbServer:

    automator = Automator(adb_server=AdbServer, adb_host="127.0.0.1", adb_port=5037)
```
##### 3. List devices
```python
for device in automator.list_devices(state=None):
    print(device.serial)

# You can instantiate an instance using your serial, if you don't want to list.
device = automator.get_device(serial="XXXXXXX")
```

##### 4. Hello World
```python
from WhatsAppManifest.automator.whatsapp import Conversation
conversation = Conversation(device=device)
jid = "0011987654321@c.us"

conversation.send_message(
            jid=jid,
            message="Hello World!",
            re_open=True, # This causes WhatsApp to close and then open again, to avoid bugs.
            wait_send_complete=True # This makes the Script only continue after the last message sent to the contact has arrived at the server or the contact.
			)
```

##### 5. Tools
```python
help(device.ui_automator)
help(device.adb_device)
help(device.adb_utils)
```
#### Attention
I'm still fixing some problems and making new features available, don't expect frequent updates because I'm using this code for learning.
I promise to improve the documentation in a few days, until then, I recommend using the examples I left in [/examples](examples "/examples").

#### Capabilities
- Send messages
- Change profile information
- Change profile photo
- Change status
- Read messages
- Get contact list
- Get list of groups
- Get all events for a given conversation

**Attention**: Part of these features are possible thanks to the possibility of manipulating the application's database, however I do not recommend that you make any changes to it, until then I only used the same for "SELECT", be careful.

#### Next steps:
- Improve documentation and facilitate access to all features, since most of them still have a little complex use
- Enable the download of files (or obtaining those already downloaded locally).

#### Special thanks for the inspiration
- [mukulhase](https://github.com/mukulhase/WebWhatsapp-Wrapper "mukulhase")
- [sigalor](https://github.com/sigalor/whatsapp-web-reveng#decryption "sigalor")
- [B16f00t](https://github.com/B16f00t/whapa/ "B16f00t")
- [robertdavidgraham](https://github.com/robertdavidgraham/whats-dec "robertdavidgraham")
- [ddz](https://github.com/ddz/whatsapp-media-decrypt "ddz")

#### Disadvantages
- Unfortunately it is not possible (or I still don't know how) to create trigger events, for example "when receiving a message activate a certain function".
- For a good flow, we almost always need to close the application and then open it again on the screen we want.

------------

### Note
This repository aims to study the language and its possibilities, not being possible a stable use of it, however this can be achieved with some development time. A warning, the misuse of this package may result in your WhatsApp account being banned.

### Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk.
