import unittest
from convert import convert
import tempfile

class TestConvert(unittest.TestCase):
    def testEmptyJsonParse(self):
        generated = convert.parse(convert._load_json_files("./jsonSamples/minimal.json")[0])

        self.assertEquals(generated.__len__(), 1)

    def testGlossaryJsonParse(self):
        generated = convert.parse(convert._load_json_files("./jsonSamples/Glossary.json")[0])

        self.assertEquals(generated.__len__(), 5)

        generated = convert.generate("Test", ["cs"], generated)
        for f in generated:
            print "".join(f["content"])