import json
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-10                                                                  #
#####################################################################################


class GlossDef:
    def __init__(self):
        self._para = ""
        self._gloss_see_also = []

    @property
    def para(self):
        """:rtype: str"""
        return self._para
    @para.setter
    def para(self, value):
        """:type value: str
           :rtype: None"""
        self._para = value

    @property
    def gloss_see_also(self):
        """:rtype: list of [str]"""
        return self._gloss_see_also
    @gloss_see_also.setter
    def gloss_see_also(self, value):
        """:type value: list of [str]
           :rtype: None"""
        self._gloss_see_also = value



    class JsonFactory():
        @staticmethod
        def to_json(self):
            """:rtype: dict"""
            return GlossDef.JsonFactory.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                d = {
                    'para': obj.para,
                    'glossSeeAlso': [],
                }
                for item in obj.gloss_see_also:
                    d['family'].append(item)

                return d

        @staticmethod
        def from_json(json_obj):
            """:type json_obj: dict
               :rtype: GlossDef"""
            obj = GlossDef()
            obj._para = json_obj["para"]
            obj._gloss_see_also = []
            for item in json_obj["glossSeeAlso"]:
                obj._gloss_see_also.append(item)
            return obj

