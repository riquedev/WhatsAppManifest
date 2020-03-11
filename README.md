# WhatsAppManifest
![GitHub](https://img.shields.io/github/license/riquedev/WhatsAppManifest)

[![codebeat badge](https://codebeat.co/badges/fa8899ba-f894-4d67-9752-f35b94778c2a)](https://codebeat.co/projects/github-com-riquedev-whatsappmanifest-master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bdbbf2c662324a28851447c62c45825a)](https://www.codacy.com/manual/rique_dev/WhatsAppManifest?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=riquedev/WhatsAppManifest&amp;utm_campaign=Badge_Grade)
[![BCH compliance](https://bettercodehub.com/edge/badge/riquedev/WhatsAppManifest?branch=master)](https://bettercodehub.com/)
[![Maintainability](https://api.codeclimate.com/v1/badges/47c3fcdd9719bd907507/maintainability)](https://codeclimate.com/repos/5e6844e143cc9c00b0000881/maintainability)
[![Known Vulnerabilities](https://snyk.io/test/github/riquedev/WhatsAppManifest/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/riquedev/WhatsAppManifest?targetFile=requirements.txt)

![GitHub contributors](https://img.shields.io/github/contributors/riquedev/WhatsAppManifest)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

![GitHub issues](https://img.shields.io/github/issues-raw/riquedev/WhatsAppManifest)
![GitHub pull requests](https://img.shields.io/github/issues-pr/riquedev/WhatsAppManifest)

[![GitHub stars](https://img.shields.io/github/stars/riquedev/WhatsAppManifest)](https://github.com/riquedev/WhatsAppManifest/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/riquedev/WhatsAppManifest)](https://github.com/riquedev/WhatsAppManifest/network)
[![HitCount](http://hits.dwyl.com/riquedev/WhatsAppManifest.svg)](http://hits.dwyl.com/riquedev/WhatsAppManifest)


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

#### Details
###### The following versions of WhatsApp are supported:
- *WhatsApp Business (com.whatsapp.w4b)* **2.20.20**
- *WhatsApp Business (com.whatsapp.w4b)* **2.20.21**

###### The following Android versions are supported:
- Android 5.1 (*API 22*) [**Emojis are not supported**]
- Android 6.0 (*API 23*)


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
- It is necessary to use more computer resources than when using the browser, for example

------------

### Note
This repository aims to study the language and its possibilities, not being possible a stable use of it, however this can be achieved with some development time. A warning, the misuse of this package may result in your WhatsApp account being banned.

### Legal
This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by WhatsApp or any of its affiliates or subsidiaries. This is an independent and unofficial software. Use at your own risk.
