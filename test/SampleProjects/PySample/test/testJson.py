import unittest
from Generated.glossary import Glossary
from Generated.person import Person
from test.GlossaryTestSetup import GlossaryTestSetup
from test.PersonTestSetup import PersonTestSetup
from testfixtures import Comparison as C


class TestJson(unittest.TestCase):
    def testLoadedPersonHasExpectedName(self):
        # Assemble
        json = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedName.person())

        # Act
        loadedPerson = Person.JsonFactory.from_json(json)

        # Assert
        C(PersonTestSetup.LoadedTestPersonHasExpectedName.person()) == loadedPerson

    def testLoadedPersonHasExpectedAge(self):
        # Assemble
        json = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedAge.person())

        # Act
        loadedPerson = Person.JsonFactory.from_json(json)

        # Assert
        C(PersonTestSetup.LoadedTestPersonHasExpectedAge.person()) == loadedPerson

    def testLoadedPersonHasExpectedCountry(self):
        # Assemble
        json = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedCountry.person())

        # Act
        loadedPerson = Person.JsonFactory.from_json(json)

        # Assert
        C(PersonTestSetup.LoadedTestPersonHasExpectedCountry.person()) == loadedPerson

    def testLoadedPersonHasExpectedFamily(self):
        # Assemble
        json = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonHasExpectedFamily.person())

        # Act
        loadedPerson = Person.JsonFactory.from_json(json)

        # Assert
        PersonTestSetup.LoadedTestPersonHasExpectedFamily.person().ToExpectedObject().ShouldMatch(loadedPerson)

    def testLoadedPersonWithMissingValues(self):
        # Assemble
        json = Person.JsonFactory.to_json(PersonTestSetup.LoadedTestPersonWithMissingValues.person())
        json.Remove("age")
        json.Remove("family")

        # Act
        loadedGlossary = Person.JsonFactory.from_json(json)

        # Assert
        C(PersonTestSetup.LoadedTestPersonWithMissingValues.person()) == loadedGlossary

    def testLoadedPersonHasNullFamily(self):
        # Assemble
        person = PersonTestSetup.LoadedTestPersonHasNullFamily.person()
        person.Family = None
        json = Person.JsonFactory.to_json(person)

        # Act
        loadedPerson = Person.JsonFactory.from_json(json)

        # Assert
        C(PersonTestSetup.LoadedTestPersonHasNullFamily.person()) == loadedPerson

    def testLoadedGlossaryHasExpectedEmptyValues(self):
        # Assemble
        json = Glossary.JsonFactory.to_json(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary())

        # Act
        loadedGlossary = Glossary.JsonFactory.from_json(json)

        # Assert
        C(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.glossary()) == loadedGlossary

    def testLoadedGlossaryWithMissingValues(self):
        # Assemble
        json = Glossary.JsonFactory.to_json(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.glossary())
        json.Remove("title")
        json["glossDiv"].Remove("title")
        json["glossDiv"]["glossList"]["glossEntry"].Remove("id")
        json["glossDiv"]["glossList"]["glossEntry"].Remove("float")

        # Act
        loadedGlossary = Glossary.JsonFactory.from_json(json)

        # Assert
        C(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.glossary()) == loadedGlossary

