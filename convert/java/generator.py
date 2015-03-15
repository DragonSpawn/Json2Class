import datetime
from convert.base.generator import BaseGenerator
from convert.base.parsedobject import ParsedObjectType


class Generator(BaseGenerator):
    def _generate_default_constructor(self):
        param = ""
        constructor = ""
        if self.data.type == ParsedObjectType.Enum:
            param = "long val"
            for member in self.data.data:
                constructor += "    public static {2} {0} = new {2}({1});\n".format(member.name.upper(), member.data, _capitalize(self.data.type_name))
            constructor = constructor[:-2] + ";\n\n"
            constructor += ("    private long value;\n"
                            "    public long getValue() { return value; }\n")
        constructor += "    public {0}({1}) {{\n".format(_capitalize(self.data.type_name), param)

        if self.data.type == ParsedObjectType.Enum:
            constructor += "        value = val;\n    }\n"
        else:
            for member in self.data.data:
                if member.type == ParsedObjectType.Array:
                    constructor += "        {0} = new ArrayList<{1}>();\n".format(member.name, _get_type_name(member.data[0], False))
                elif member.type == ParsedObjectType.Enum:
                    constructor += "        {0} = new {1}(0);\n".format(member.name, _get_type_name(member))
                elif member.type == ParsedObjectType.String:
                    constructor += "        {0} = \"\";\n".format(member.name)

            constructor += "    }\n"
        return constructor

    def _generate_footer(self):
        result = ""
        if self.data.type == ParsedObjectType.Enum:
            result += ("    @Override\n"
                       "    public boolean equals(Object o) {\n"
                       "        if (this == o) return true;\n"
                       "        if (o == null || getClass() != o.getClass()) return false;\n"
                       "\n"
                       "        Gender gender = (Gender) o;\n"
                       "\n"
                       "        return value == gender.value;\n"
                       "    }\n"
                       "\n"
                       "    @Override\n"
                       "    public int hashCode() {\n"
                       "        return (int) (value ^ (value >>> 32));\n"
                       "    }\n")
        return result + "}\n"

    def _generate_member_access(self):
        if self.data.type == ParsedObjectType.Enum:
            return ""
        properties = ""
        for member in self.data.data:
            properties += _member_declaration(member)
        return properties

    def file_name(self, name):
        return name[0].upper() + name[1:] + ".java"

    def _generate_header(self):
        result = "package {0};\n\n".format(self.namespace)

        if self.data.type != ParsedObjectType.Enum:
            for factory in self.factories:
                result += factory.generate_import()

        date_str = "Date: {0}".format(datetime.date.today())
        if BaseGenerator.skip_date_comment:
            date_str = ""
        date_str = date_str.ljust(80)
        result += ("/***********************************************************************************/\n"
                   "/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/\n"
                   "/* Modifications to this file will be lost the next time you run the tool.         */\n"
                   "/* {2}*/\n"
                   "/***********************************************************************************/\n\n"
                   "public class {1}{{\n").format(self.namespace, _capitalize(self.data.type_name), date_str)
        return result


def _member_declaration(member):
    return "    public {0} {1};\n".format(_get_type_name(member), member.name)


def _capitalize(obj):
    """
    Returns the object name with the first letter capitalized (all other untouched).
    :param obj:
    :return:
    """
    if obj.__len__() < 2:
        return obj
    if obj == "string" or obj == "float" or obj == "int":
        return obj
    return obj[0].upper() + obj[1:]


def _get_type_name(member, primitive=True):
    """
    If a ParsedClass is supplied then it returns the object name with a captialized first letter (myClass => MyClass)
    For ParsedMember it returns the type of the member (myString => string)
    :type member: ParsedMember
    :param obj:
    :return:
    """
    if member.type == ParsedObjectType.String:
        return "String"
    if member.type == ParsedObjectType.Int or member.type == ParsedObjectType.Float or member.type == ParsedObjectType.Bool:
        if member.type == ParsedObjectType.Int:
            return "Long"
        elif member.type == ParsedObjectType.Float:
            return "Float"
        elif member.type == ParsedObjectType.Bool:
                return "Boolean"
        return member.type.name.lower()
    if member.type == ParsedObjectType.Array:
        return "List<{0}>".format(_get_type_name(member.data[0], False))
    return _capitalize(member.type_name)