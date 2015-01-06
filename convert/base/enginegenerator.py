
class BaseEngineGenerator():
    def __init__(self):
        self.namespace = ""

    def generate(self, namespace):
        self.namespace = namespace
        return "".join([
            self._generate_header(),
            self._generate_read_string(),
            self._generate_read_int(),
            self._generate_read_float(),
            self._generate_read_bool(),
            self._generate_read_array(),
            self._generate_write_string(),
            self._generate_write_int(),
            self._generate_write_float(),
            self._generate_write_bool(),
            self._generate_write_array(),
            self._generate_footer()
        ])

    def file_name(self):
        raise NotImplementedError()

    def _generate_header(self):
        raise NotImplementedError()

    def _generate_read_string(self):
        raise NotImplementedError()

    def _generate_read_int(self):
        raise NotImplementedError()

    def _generate_read_float(self):
        raise NotImplementedError()

    def _generate_read_bool(self):
        raise NotImplementedError()

    def _generate_write_string(self):
        raise NotImplementedError()

    def _generate_write_int(self):
        raise NotImplementedError()

    def _generate_write_float(self):
        raise NotImplementedError()

    def _generate_write_bool(self):
        raise NotImplementedError()

    def _generate_read_array(self):
        raise NotImplementedError()

    def _generate_write_array(self):
        raise NotImplementedError()

    def _generate_footer(self):
        raise NotImplementedError()