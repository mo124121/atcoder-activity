from multiprocessing.managers import SyncManager
import unittest
from unittest.mock import Mock


class TestChatAcceptance:
    def test_message_exchange(self):
        user1 = ChatClient("yamada")
        user2 = ChatClient("sato")

        user1.send_message("hello")
        messages = user2.fetch_messages()

        assert messages == ["yamada: hello"]


class TestChatClient(unittest.TestCase):
    def test_nickname(self):
        client = ChatClient("User 1")
        assert client.nickname == "User 1"

    def test_send_message(self):
        client = ChatClient("User 1")
        client.connection = Mock()
        sent_message = client.send_message("Hello World")
        assert sent_message == "User 1: Hello World"

    def test_client_connection(self):
        client = ChatClient("User 1")
        connection_spy = unittest.mock.MagicMock()
        with unittest.mock.patch.object(
            client, "_get_connection", retrun_value=connection_spy
        ):
            client.sent_message("Hello World")
        connection_spy.broadcast.assert_called_with(("User 1: Hello World"))


class ChatClient:
    def __init__(self, nickname):
        self.nickname = nickname

    def send_message(self, message):
        sent_message = "{}: {}".format(self.nickname, message)
        self.connection.broadcast(message)
        return sent_message


class Connection(SyncManager):
    def __init__(self, address):
        self.register("get_messages")
        super().__init__(address=address, authkey=b"mychatsecret")
        self.connect()

    def broadcast(self, message):
        messages = self.get_messages()
        messages.append(message)


class TestConnection:
    def test_broadcast(self):
        """check able to send messange after conecction established"""

        with unittest.mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))

        with unittest.mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("some message")
            assert c.get_messages()[-1] == "some message"
