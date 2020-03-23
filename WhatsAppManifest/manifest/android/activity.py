from collections import namedtuple
ActivitiesTuple = namedtuple("Activities", [
    "WhatsAppConversation",
    "WhatsAppGalleryPickerMediaPreview",
    "WhatsAppContactPicker"
])

Activities = ActivitiesTuple(
    "com.whatsapp.Conversation",
    "com.whatsapp.gallerypicker.MediaPreviewActivity",
    "com.whatsapp.ContactPicker"
)
