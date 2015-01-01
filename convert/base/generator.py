
class BaseGenerator():
    """
    This is the generator base class which is basically just a set of methods that should be implemented for the
    different languages
    """
    def __init__(self):
        pass

    def generateCode(self, data):
        raise NotImplementedError()