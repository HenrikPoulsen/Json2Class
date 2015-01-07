
class BaseFactoryGenerator():
    def __init__(self):
        self.data = None
        self.namespace = None

    def init(self, data, namespace):
        self.data = data
        self.namespace = namespace

    def generate_import(self):
        raise NotImplementedError()

    def generate(self, data, namespace):
        raise NotImplementedError()

    def _generate_to_json(self):
        raise NotImplementedError()

    def _generate_from_json(self):
        raise NotImplementedError()