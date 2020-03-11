from WhatsAppManifest import ADB


with ADB(use_ssh=True,
         ssh_ip="<SSH-IP>",
         ssh_port=22,
         ssh_username="<SSH-USERNAME>",
         ssh_password="<SSH-PASSWORD>",
         remote_bind_ip="127.0.0.1",  # ADB SERVER INTERNAL IP
         remote_bind_port=5037  # ADB SERVER PORT
         ) as AdbServer:

    help(AdbServer)

