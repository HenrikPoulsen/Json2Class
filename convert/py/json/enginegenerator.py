from convert.base.enginegenerator import BaseEngineGenerator


class EngineGenerator(BaseEngineGenerator):

    def file_name(self):
        return "json2class.py"

    def _generate_write_int(self):
        return ""

    def _generate_write_object(self):
        return ""

    def _generate_read_object(self):
        return ""

    def _generate_write_string(self):
        return ""

    def _generate_write_bool(self):
        return ""

    def _generate_read_string(self):
        return ""

    def _generate_header(self):
        return ""

    def _generate_read_float(self):
        return ""

    def _generate_read_int(self):
        return ""

    def _generate_read_bool(self):
        return ""

    def _generate_write_float(self):
        return ""
