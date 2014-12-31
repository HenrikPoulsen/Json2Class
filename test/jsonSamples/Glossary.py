class Glossary:
    def __init__(self):
        self._GlossSeeAlso = []
        self._para = ""
        self._GlossSee = ""
        self._Acronym = ""
        self._GlossTerm = ""
        self._Abbrev = ""
        self._SortAs = ""
        self._ID = ""
        self._title = ""
        self._id = 0
        self._title = ""
    @property
    def GlossSeeAlso(self):
        return self._GlossSeeAlso
    @GlossSeeAlso.setter
    def GlossSeeAlso(self, value):
        self._GlossSeeAlso = value

    @property
    def para(self):
        return self._para
    @para.setter
    def para(self, value):
        self._para = value

    @property
    def GlossSee(self):
        return self._GlossSee
    @GlossSee.setter
    def GlossSee(self, value):
        self._GlossSee = value

    @property
    def Acronym(self):
        return self._Acronym
    @Acronym.setter
    def Acronym(self, value):
        self._Acronym = value

    @property
    def GlossTerm(self):
        return self._GlossTerm
    @GlossTerm.setter
    def GlossTerm(self, value):
        self._GlossTerm = value

    @property
    def Abbrev(self):
        return self._Abbrev
    @Abbrev.setter
    def Abbrev(self, value):
        self._Abbrev = value

    @property
    def SortAs(self):
        return self._SortAs
    @SortAs.setter
    def SortAs(self, value):
        self._SortAs = value

    @property
    def ID(self):
        return self._ID
    @ID.setter
    def ID(self, value):
        self._ID = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        self._title = value