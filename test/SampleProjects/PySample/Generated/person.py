import json
from gender import Gender
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
#                                                                                   #
#####################################################################################


class Person(object):
    def __init__(self):
        self._name = ""
        self._age = 0
        self._country = ""
        self._is_human = False
        self._gender = Gender(0)
        self._family = []

    @property
    def name(self):
        """:rtype: str"""
        return self._name

    @name.setter
    def name(self, value):
        """:type value: str
           :rtype: None"""
        self._name = value

    @property
    def age(self):
        """:rtype: int"""
        return self._age

    @age.setter
    def age(self, value):
        """:type value: int
           :rtype: None"""
        self._age = value

    @property
    def country(self):
        """:rtype: str"""
        return self._country

    @country.setter
    def country(self, value):
        """:type value: str
           :rtype: None"""
        self._country = value

    @property
    def is_human(self):
        """:rtype: bool"""
        return self._is_human

    @is_human.setter
    def is_human(self, value):
        """:type value: bool
           :rtype: None"""
        self._is_human = value

    @property
    def gender(self):
        """:rtype: Gender"""
        return self._gender

    @gender.setter
    def gender(self, value):
        """:type value: Gender
           :rtype: None"""
        self._gender = value

    @property
    def family(self):
        """:rtype: list of [Person]"""
        return self._family

    @family.setter
    def family(self, value):
        """:type value: list of [Person]
           :rtype: None"""
        self._family = value

    class JsonFactory():
        def __init__(self):
            pass

        @staticmethod
        def to_json(self):
            """:rtype: str"""
            return Person.JsonFactory.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                if obj is None:
                    return None
                d = {
                    'name': obj.name,
                    'age': obj.age,
                    'country': obj.country,
                    'isHuman': obj.is_human,
                    'gender': obj.gender.value,
                    'family': [],
                }
                for item in obj.family:
                    d['family'].append(Person.JsonFactory.JsonEncoder().default(item))

                return d

        @staticmethod
        def from_json(json_obj):
            """:type json_obj: dict
               :rtype: Person"""
            if json_obj is None:
                return None
            obj = Person()
            if "name" in json_obj:
                obj._name = json_obj["name"]
            if "age" in json_obj:
                obj._age = json_obj["age"]
            if "country" in json_obj:
                obj._country = json_obj["country"]
            if "isHuman" in json_obj:
                obj._is_human = json_obj["isHuman"]
            if "gender" in json_obj:
                obj._gender = Gender(json_obj["gender"])
            if "family" in json_obj:
                obj._family = []
                for item in json_obj["family"]:
                    obj._family.append(Person.JsonFactory.from_json(item))
            return obj

