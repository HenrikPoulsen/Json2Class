import unittest
from convert import convert
from convert.base.parsedobject import *


class TestParsedObject(unittest.TestCase):
    def testParsePerson(self):
        json = convert._load_json_files("./jsonSamples/Person.json")[0]["content"]

        obj = ParsedObject("Person", json)
        print obj