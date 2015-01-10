from Generated.person import Person


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
            person.age = 100;
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
            person.family = []

            temp_person = Person()
            temp_person.name = "Family"
            temp_person.age = -1
            temp_person.country = "Random"
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

