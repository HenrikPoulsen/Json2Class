
class BaseFactoryGenerator():
    def __init__(self):
        self.data = None

    def generate(self, data):
        raise NotImplementedError()