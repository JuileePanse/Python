from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

    def __init__(self, users):
        self.users = users
        self.name = None
        self.state = "GETNAME" #initial state

    def connectionMade(self):
        temp= str("What's your name?")
        self.sendLine(temp.encode("utf-8"))

    def connectionLost(self, reason):
        if self.name in self.users:
            del self.users[self.name]

    def lineReceived(self, line):
        if self.state == "GETNAME":
            self.handle_GETNAME(line.decode())
        else:
            self.handle_CHAT(line.decode())

    def handle_GETNAME(self, name):
        if name in self.users:
            temp= str("Name taken, please choose another.")
            self.sendLine(temp.encode("utf-8"))
            return
        temp_send = str("Welcome, %s!" % (name))
        self.sendLine(temp_send.encode("utf-8"))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):
        #while message != 'bye':
        message = "<%s> %s" % (self.name, message)
        for name, protocol in self.users.items():
            # Send the message to all other users.
            # This allows to have multiple chats.
            if protocol != self:
                protocol.sendLine(message.encode("utf-8"))


class ChatFactory(Factory):

    def __init__(self):
        self.users = {} # maps user names to Chat instances

    def buildProtocol(self, addr):
        # Create a seperate Chat for each user
        return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()