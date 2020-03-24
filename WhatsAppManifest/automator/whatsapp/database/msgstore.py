import re
from typing import Iterator
from WhatsAppManifest.consts import _MESSAGE_IS_SENT_
from WhatsAppManifest.automator.whatsapp.database.objects import Jid, Chat, Message
from WhatsAppManifest.manifest.whatsapp.path import Path
from WhatsAppManifest.automator.whatsapp.database.base import WhatsAppDatabase


class WhatsAppDatabaseMSGStore(WhatsAppDatabase):
    """
        WhatsApp MSGStore Database
    """
    _database = Path.msgstore

    def get_jid(self, _id: str) -> Jid:
        """
        Get Jid object from a valid id
        :param _id: Valid ID
        :type _id: str
        :return: Jid object
        :rtype: Jid
        """
        return Jid(self.query(f"SELECT * FROM jid where _id = '{_id}'")[0])

    @property
    def jid_groups(self) -> Iterator[Jid]:
        """
        Get all Jid objects for WhatsApp groups
        :return: Jid Iterator
        :rtype: Iterator[Jid]
        """
        return map(lambda row: Jid(row), self.query(f"SELECT * FROM jid where type = '1'"))

    @property
    def jid_users(self) -> Iterator[Jid]:
        """
        Get all Jid objects for WhatsApp users
        :return: Jid Iterator
        :rtype: Iterator[Jid]
        """
        return map(lambda row: Jid(row), self.query(f"SELECT * FROM jid where type = '0'"))

    @property
    def jids(self) -> Iterator[Jid]:
        """
        Gets all Jid objects
        :return: Jid Iterator
        :rtype: Iterator[Jid]
        """
        return map(lambda row: Jid(row), self.get_all_rows("jid"))

    def get_jid_from_number(self, phone: str) -> Jid:
        """
        Get a Jid object from a phone
        :param phone: Valid phone number (only numbers)
        :type phone: str
        :return: Jid object
        :rtype: Jid
        """
        phone = re.sub("[^0-9]", "", phone)
        for jid in map(lambda row: Jid(row), self.query(f"SELECT * FROM jid where user = '{phone}'")):
            return jid

    @property
    def chat(self) -> Iterator[Chat]:
        """
        Returns all chats
        :return: Iterator of Chat
        :rtype: Iterator[Chat]
        """
        return map(lambda row: Chat(row), self.get_all_rows("chat"))

    @property
    def messages(self) -> Iterator[Message]:
        """
        Returns all messages
        :return: Iterator of Message
        :rtype: Iterator[Message]
        """
        return map(lambda row: Message(row), self.get_all_rows("messages"))

    @property
    def last_messages(self) -> Iterator[Message]:
        """
        Returns the last message of all conversations
        :return: Iterator of Message
        :rtype: Iterator[Message]
        """
        for row in self.query("select * from messages where _id in (SELECT last_message_row_id FROM chat)"):
            yield Message(row)

    def contact_messages(self, jid: str) -> Iterator[Message]:
        """
        Returns all messages from the respective contact
        :param jid: JID id of user
        :type jid: str
        :return: Iterator of Message
        :rtype: Iterator[Message]
        """

        for sub_row in self.query(f"SELECT * from messages where key_remote_jid = '{jid}'"):
            return Message(sub_row)

    def last_contact_message(self, jid: str) -> Message:
        """
        Get last message from a respective contact
        :param jid: JID id of user
        :type jid: str
        :return: Message
        :rtype: Message
        """
        for row in self.query(
                f"select * from messages where _id in (SELECT last_message_row_id FROM chat where jid_row_id in (SELECT _id from jid where raw_string = '{jid}'))"):
            return Message(row)

    def chat_last_message_has_sent(self, jid: str) -> bool:
        has_sent = False

        for row in self.query(
                f"select * from messages where _id in (SELECT last_message_row_id FROM chat where jid_row_id in (SELECT _id from jid where raw_string = '{jid}'))"):
            message = Message(row)

            if message is not None:
                has_sent = _MESSAGE_IS_SENT_(message.status)
            break

        return has_sent

    def chat_exists(self, jid) -> bool:
        for row in self.query(
                f"""SELECT _id from chat where jid_row_id in (SELECT _id from jid where raw_string = '{jid}')"""
        ):
            return row is not None
        return False
