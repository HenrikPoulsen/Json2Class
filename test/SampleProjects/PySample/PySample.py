import json
from Generated.person import Person


def main():
    loaded_json = json.load(open("../../jsonSamples/Person.json"))
    person = Person.JsonFactory.from_json(loaded_json)
    print person.age
    print person.family.__len__()

    print loaded_json
    print Person.JsonFactory.to_json(person)


main()
