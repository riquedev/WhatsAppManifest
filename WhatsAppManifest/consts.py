# This Python package supports this android application
_PACKAGE_NAME_ = "com.whatsapp.w4b"

# Supported versions of the application
_PACKAGE_VERSION_SUPPORT_ = [
    "2.20.20","2.20.21","2.20.22",
    "2.20.23","2.20.24"
]

# The package supports these versions of the android device
_ANDROID_VERSION_SUPPORT_ = [
    "5.1","6.0"
]

# This package supports these versions of the Android SDK
_SDK_LEVEL_SUPPORT_ = [
    "22","23"
]

# This package supports these versions of Android Debug Bridge
_ADB_VERSIONS_SUPPORTED_ = [
    "40","41"
]

# Checking functions
_PACKAGE_VERSION_ = lambda vers: str(vers) in _PACKAGE_VERSION_SUPPORT_
_ADB_VERSION_ = lambda vers: str(vers) in _ADB_VERSIONS_SUPPORTED_
_ANDROID_VERSION_ = lambda vers: str(vers) in _ANDROID_VERSION_SUPPORT_
_SDK_LEVEL_ = lambda level: str(level) in _SDK_LEVEL_SUPPORT_
