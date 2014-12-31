import unittest
from convert import convert
import tempfile

class TestConvert(unittest.TestCase):
    def testEmptyJson(self):
        targets = ['py', 'cs']
        generated = convert.generate("Test", targets, convert._load_json_files("./jsonSamples/minimal.json")[0])

        self.assertGreater(generated.__len__(), 0)
        self.assertEquals(generated.keys(), ['minimal.cs', 'minimal.py'])

    def testGlossaryJson(self):
        targets = ['py', 'cs']
        generated = convert.generate("Test", targets, convert._load_json_files("./jsonSamples/Glossary.json")[0])

        print "".join(generated["Glossary.cs"]["generated"])
        print "".join(generated["glossary.py"]["generated"])
        self.assertGreater(generated.__len__(), 0)
        self.assertEquals(generated.keys(), ['Glossary.cs', 'glossary.py'])