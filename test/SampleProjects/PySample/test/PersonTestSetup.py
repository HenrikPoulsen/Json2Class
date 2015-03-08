from testfixtures.comparison import register
from Generated.person import Person
from testfixtures import compare
from Generated.gender import Gender


def compare_person(x, y, context):
    """

    :type x: Person
    :type y: Person
    """
    if x.gender != y.gender:
        return "Person {0} gender {1} != Person {2} gender {3}".format(x.name, x.gender, y.name, y.gender)
    if x.name != y.name:
        return "Person name {0} != Person name {1}".format(x.name, y.name)
    if x.age != y.age:
        return "Person {0} age {1} != Person {2} age {3}".format(x.name, x.age, y.name, y.age)
    if x.country != y.country:
        return "Person {0} country {1} != Person {2} country {3}".format(x.name, x.country, y.name, y.country)
    return compare(x.family, y.family)

register(Person, compare_person)


class PersonTestSetup:
    class LoadedTestPersonHasExpectedName:
        @staticmethod
        def person():
            person = Person()
            person.name = "Hello"
            return person

    class LoadedTestPersonHasExpectedAge:
        @staticmethod
        def person():
            person = Person()
            person.age = 100
            return person

    class LoadedTestPersonHasExpectedCountry:
        @staticmethod
        def person():
            person = Person()
            person.country = "ExpectedCountry"
            return person

    class LoadedTestPersonHasExpectedFamily:
        @staticmethod
        def person():
            person = Person()
            person.name = "Empty"
            person.age = 10
            person.country = "Whatever"
            person.gender = Gender.Male
            person.family = []

            temp_person = Person()
            temp_person.name = "Family"
            temp_person.age = -1
            temp_person.country = "Random"
            temp_person.gender = Gender.Female
            person.family.append(temp_person)
            person.family.append(Person())
            return person

    class LoadedTestPersonHasNullFamily:
        @staticmethod
        def person():
            person = Person()
            person.name = "Empty"
            person.age = 10
            person.country = "Whatever"
            person.family = []
            return person

    class LoadedTestPersonWithMissingValues:
        @staticmethod
        def person():
            return Person()

    class LoadedTestPersonListAsExpected:
        @staticmethod
        def people():
            people = [Person(), Person()]
            people[0].age = 3
            people[0].country = "DK"
            people[0].is_human = True
            people[0].name = "Olle"
            people[1].age = 187
            people[1].country = "NA"
            people[1].is_human = False
            people[1].name = "Splork"
            return people
