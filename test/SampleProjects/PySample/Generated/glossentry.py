import json
from glossdef import GlossDef
#####################################################################################
# This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)  #
# Modifications to this file will be lost the next time you run the tool.           #
# Date: 2015-01-07                                                                  #
#####################################################################################


class GlossEntry:
    def __init__(self):
        self._id = 0
        self._test_float = 0.0
        self._sort_as = ""
        self._gloss_term = ""
        self._acronym = ""
        self._abbrev = ""
        self._gloss_def = None
        self._gloss_see = ""

    @property
    def id(self):
        """:rtype: int"""
        return self._id
    @id.setter
    def id(self, value):
        """:type value: int
           :rtype: None"""
        self._id = value

    @property
    def test_float(self):
        """:rtype: float"""
        return self._test_float
    @test_float.setter
    def test_float(self, value):
        """:type value: float
           :rtype: None"""
        self._test_float = value

    @property
    def sort_as(self):
        """:rtype: str"""
        return self._sort_as
    @sort_as.setter
    def sort_as(self, value):
        """:type value: str
           :rtype: None"""
        self._sort_as = value

    @property
    def gloss_term(self):
        """:rtype: str"""
        return self._gloss_term
    @gloss_term.setter
    def gloss_term(self, value):
        """:type value: str
           :rtype: None"""
        self._gloss_term = value

    @property
    def acronym(self):
        """:rtype: str"""
        return self._acronym
    @acronym.setter
    def acronym(self, value):
        """:type value: str
           :rtype: None"""
        self._acronym = value

    @property
    def abbrev(self):
        """:rtype: str"""
        return self._abbrev
    @abbrev.setter
    def abbrev(self, value):
        """:type value: str
           :rtype: None"""
        self._abbrev = value

    @property
    def gloss_def(self):
        """:rtype: GlossDef"""
        return self._gloss_def
    @gloss_def.setter
    def gloss_def(self, value):
        """:type value: GlossDef
           :rtype: None"""
        self._gloss_def = value

    @property
    def gloss_see(self):
        """:rtype: str"""
        return self._gloss_see
    @gloss_see.setter
    def gloss_see(self, value):
        """:type value: str
           :rtype: None"""
        self._gloss_see = value



    class JsonFactory():
        @staticmethod
        def to_json(self):
            """:rtype: dict"""
            return GlossEntry.JsonEncoder().encode(self)

        class JsonEncoder(json.JSONEncoder):
            def default(self, obj):
                d = {
                    'id': obj.id,
                    'testFloat': obj.test_float,
                    'sortAs': obj.sort_as,
                    'glossTerm': obj.gloss_term,
                    'acronym': obj.acronym,
                    'abbrev': obj.abbrev,
                    'glossDef': obj.gloss_def.to_json(),
                    'glossSee': obj.gloss_see,
                }
                return d

        @staticmethod
        def from_json(cls, json_obj):
            """:type json_obj: dict
               :rtype: GlossEntry"""
            obj = GlossEntry()
            obj._id = json_obj["id"]
            obj._test_float = json_obj["testFloat"]
            obj._sort_as = json_obj["sortAs"]
            obj._gloss_term = json_obj["glossTerm"]
            obj._acronym = json_obj["acronym"]
            obj._abbrev = json_obj["abbrev"]
            obj._gloss_def = GlossDef(json_obj["glossDef"])
            obj._gloss_see = json_obj["glossSee"]
            return obj

