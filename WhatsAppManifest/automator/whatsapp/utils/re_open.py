from WhatsAppManifest.adb.device import Device


def re_open_package(device: Device, package: str) -> tuple:
    app_stop = device.adb_utils.app_stop(package)
    app_start = device.adb_utils.app_start(package)
    return (
        app_stop,
        app_start
    )
