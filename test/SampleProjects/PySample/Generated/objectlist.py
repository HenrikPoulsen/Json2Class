import json
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-09                                                                  #
#####################################################################################


class ObjectList:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        """:rtype: str"""
        return self._name
    @name.setter
    def name(self, value):
        """:type value: str
           :rtype: None"""
        self._name = value



    class JsonFactory():
        @staticmethod
        def to_json(self):
            """:rtype: dict"""
            return ObjectList.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                d = {
                    'name': obj.name,
                }
                return d

        @staticmethod
        def from_json(cls, json_obj):
            """:type json_obj: dict
               :rtype: ObjectList"""
            obj = ObjectList()
            obj._name = json_obj["name"]
            return obj

