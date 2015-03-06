from convert.base.parsedobject import ParsedObjectType
from factorygenerator import BaseFactoryGenerator


class BaseGenerator():
    """
    This is the generator base class which is basically just a set of methods that should be implemented for the
    different languages
    """
    skip_date_comment = False

    def __init__(self, factories):
        """

        :type engines: list of BaseFactoryGenerator
        :return:
        """
        self.data = None
        self.namespace = ""
        self.engines = []
        self.factories = factories

    def generate_code(self, namespace, data):
        """
        Returns a string representing a class that can load/save the content of the json the ParsedObject is based on.
        :param data: ParsedObject
        :return:
        """
        self.data = data
        self.namespace = namespace

        for factory in self.factories:
            factory.init(self.data, self.namespace)

        result = "".join(
        [
            self._generate_header(),
            self._generate_default_constructor(),
            self._generate_member_access(),
            self._generate_factory(),
            self._generate_footer()
        ])
        return result

    def file_name(self, name):
        """
        Gets an appropriate file name for the current generator language
        :type name: str
        :rtype: str
        :return:
        """
        raise NotImplementedError()

    def _generate_header(self):
        """
        The class definition and any includes/imports/etc that goes in the top of the file
        :rtype: string
        :return:
        """
        raise NotImplementedError()

    def _generate_default_constructor(self):
        """
        A default constructor so that you can create an instance of the class without having to load it from a json object
        :rtype: string
        :return:
        """
        raise NotImplementedError()

    def _generate_json_constructor(self):
        """
        Code for a constructor which accepts a json object and then loads the content into the appropriate members
        :rtype: string
        :return:
        """
        raise NotImplementedError()

    def _generate_member_access(self):
        """
        Code for getting/setting the members in the class
        :rtype: string
        :return:
        """
        raise NotImplementedError()

    def _generate_factory(self):
        """
        Code for a function which converts a class instance to a Json Object
        :rtype: string
        :return:
        """
        # Enums don't need factories
        if self.data.type == ParsedObjectType.Enum:
            return ""
        result = ""
        for factory in self.factories:
            result += factory.generate(self.data, self.namespace)
        return result

    def _generate_footer(self):
        """
        Returns a string representing the end of the class file
        :rtype: string
        :return:
        """
        raise NotImplementedError()