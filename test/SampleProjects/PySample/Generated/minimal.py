import json
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-09                                                                  #
#####################################################################################


class Minimal:
    def __init__(self):
        pass



    class JsonFactory():
        @staticmethod
        def to_json(self):
            """:rtype: dict"""
            return Minimal.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                d = {
                }
                return d

        @staticmethod
        def from_json(cls, json_obj):
            """:type json_obj: dict
               :rtype: Minimal"""
            obj = Minimal()
            return obj

