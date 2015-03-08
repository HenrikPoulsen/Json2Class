import unittest
import json
import sys
from Generated.glossary import Glossary
from Generated.person import Person
from test.GlossaryTestSetup import GlossaryTestSetup
from test.PersonTestSetup import PersonTestSetup
from testfixtures import Comparison
from testfixtures import compare



class TestJson(unittest.TestCase):

    def testLoadedPersonHasExpectedName(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedName.person())
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        self.assertEqual(Comparison(PersonTestSetup.LoadedTestPersonHasExpectedName.person()), loaded_person)

    def testLoadedPersonHasExpectedAge(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedAge.person())
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        expected_object = PersonTestSetup.LoadedTestPersonHasExpectedAge.person()
        compare(expected_object, loaded_person)

    def testLoadedPersonHasExpectedCountry(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedCountry.person())
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        self.assertEqual(Comparison(PersonTestSetup.LoadedTestPersonHasExpectedCountry.person()), loaded_person)

    def testLoadedPersonHasExpectedFamily(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedFamily.person())
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        expected_person = PersonTestSetup.LoadedTestPersonHasExpectedFamily.person()
        compare(expected_person, loaded_person, strict=True)

    def testLoadedPersonWithMissingValues(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonWithMissingValues.person())
        json_str = json_str.replace(", \"age\": 0", "")
        json_str = json_str.replace(", \"family\": []", "")
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        compare(PersonTestSetup.LoadedTestPersonWithMissingValues.person(), loaded_person, strict=True)

    def testLoadedPersonHasNullFamily(self):
        # Assemble
        person = PersonTestSetup.LoadedTestPersonHasNullFamily.person()
        person.Family = None
        json_str = Person.JsonFactory.to_json(person)
        json_obj = json.loads(json_str)

        # Act
        loaded_person = Person.JsonFactory.from_json(json_obj)

        # Assert
        compare(PersonTestSetup.LoadedTestPersonHasNullFamily.person(), loaded_person)

    def testLoadedGlossaryHasExpectedEmptyValues(self):
        # Assemble
        json_str = Glossary.JsonFactory.to_json(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary())
        json_obj = json.loads(json_str)

        # Act
        loaded_glossary = Glossary.JsonFactory.from_json(json_obj)

        # Assert
        compare(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary(), loaded_glossary)

    def testLoadedGlossaryWithMissingValues(self):
        # Assemble
        json_str = Glossary.JsonFactory.to_json(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.glossary())
        json_obj = json.loads(json_str)
        json_obj.pop("title", None)
        json_obj["glossDiv"].pop("title", None)
        json_obj["glossDiv"]["glossList"]["glossEntry"].pop("id", None)
        json_obj["glossDiv"]["glossList"]["glossEntry"].pop("float", None)

        # Act
        loaded_glossary = Glossary.JsonFactory.from_json(json_obj)

        # Assert
        expected_object = GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.glossary()
        compare(expected_object, loaded_glossary)

    def testLoadedGlossaryMismatchedValues(self):
        # Assemble
        json_str = Glossary.JsonFactory.to_json(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary())
        json_obj = json.loads(json_str)

        # Act
        loaded_glossary = Glossary.JsonFactory.from_json(json_obj)
        loaded_glossary.title = "Different"

        # Assert
        try:
            compare(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary(), loaded_glossary)
        except AssertionError as err:
            self.assertEqual("Glossary title  != Glossary title Different", err.message)

    def testLoadedPeopleAsExpected(self):
        # Assemble
        json_str = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonListAsExpected.people())
        json_obj = json.loads(json_str)

        # Act
        loaded_people = Person.JsonFactory.from_json_array(json_obj)

        # Assert
        i = 0
        while i < len(loaded_people):
            self.assertEqual(Comparison(PersonTestSetup.LoadedTestPersonListAsExpected.people()[i]), loaded_people[i])
            i += 1


def _get_dict(obj):
    if obj is None:
        return None
    d = obj.__dict__
    for key in d:
        value = d[key]
        t = type(value)
        if isinstance(value, (str, unicode, int, long, float, complex, dict)):
            print "ignore"
        else:
            d[key] = _get_dict(value)
        print key
    return d
