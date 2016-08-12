class Command(object):

    desc = ''
    usage = ''
    names = []
    roles = []

    def __init__(self, desc, usage, names, roles):
        self.desc = desc
        self.usage = usage
        self.names = names
        self.roles = roles
        pass

    def getDescription(self):
        return self.desc

    def getUsage(self):
        return self.usage

    def getNames(self):
        return self.names

    def getRoles(self):
        return self.roles

    def onCommand(self, message, args):
        raise NotImplementedError()
