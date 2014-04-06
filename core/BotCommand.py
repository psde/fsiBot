
class BotCommand(object):
    UNKNOWN = 0
    PRIVATE = 1
    PUBLIC = 2

    def __init__(self, bot, origin, commandType, command, args):
        self.bot = bot
        self.origin = origin
        self.type = commandType
        self.command = command
        self.args = args

    def answer(self, message):
        if self.type == BotCommand.UNKNOWN:
            return
        if self.type == BotCommand.PRIVATE:
            self.bot.sendPrivateMessage(self.origin, message)
        if self.type == BotCommand.PUBLIC:
            self.bot.sendPublicMessage(message)