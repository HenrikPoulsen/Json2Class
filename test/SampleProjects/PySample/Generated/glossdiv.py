import json
from glosslist import GlossList
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
#                                                                                   #
#####################################################################################


class GlossDiv(object):
    def __init__(self):
        self._title = ""
        self._gloss_list = None

    @property
    def title(self):
        """:rtype: str"""
        return self._title

    @title.setter
    def title(self, value):
        """:type value: str
           :rtype: None"""
        self._title = value

    @property
    def gloss_list(self):
        """:rtype: GlossList"""
        return self._gloss_list

    @gloss_list.setter
    def gloss_list(self, value):
        """:type value: GlossList
           :rtype: None"""
        self._gloss_list = value

    class JsonFactory():
        def __init__(self):
            pass

        @staticmethod
        def to_json(self):
            """:rtype: str"""
            return GlossDiv.JsonFactory.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                if obj is None:
                    return None
                d = {
                    'title': obj.title,
                    'glossList': GlossList.JsonFactory.JsonEncoder().default(obj.gloss_list),
                }
                return d

        @staticmethod
        def from_json(json_obj):
            """:type json_obj: dict
               :rtype: GlossDiv"""
            if json_obj is None:
                return None
            obj = GlossDiv()
            if "title" in json_obj:
                obj._title = json_obj["title"]
            if "glossList" in json_obj:
                obj._gloss_list = GlossList.JsonFactory.from_json(json_obj["glossList"])
            return obj

