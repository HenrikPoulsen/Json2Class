from testfixtures import compare
from testfixtures.comparison import register
from Generated.glossary import Glossary
from Generated.glossdef import GlossDef
from Generated.glossdiv import GlossDiv
from Generated.glossentry import GlossEntry
from Generated.glosslist import GlossList


def compare_glossary(x, y, context):
    """
    :type x: Glossary
    :type y: Glossary
    """
    if x.title != y.title:
        return "Glossary title {0} != Glossary title {1}".format(x.title, y.title)
    return compare(x.gloss_div, y.gloss_div)


def compare_gloss_div(x, y, context):
    """
    :type x: GlossDiv
    :type y: GlossDiv
    """
    if x.title != y.title:
        return "GlossDiv title {0} != GlossDiv title {1}".format(x.title, y.title)
    return compare(x.gloss_list, y.gloss_list)


def compare_gloss_list(x, y, context):
    """
    :type x: GlossList
    :type y: GlossList
    """
    return compare(x.gloss_entry, y.gloss_entry)


def compare_gloss_entry(x, y, context):
    """
    :type x: GlossEntry
    :type y: GlossEntry
    """
    if x.id != y.id:
        return "GlossEntry id {0} != GlossEntry id {1}".format(x.id, y.id)
    if x.test_float != y.test_float:
        return "GlossEntry {0} test_float {2} != GlossEntry {1} test_float {3}".format(x.id, y.id, x.test_float, y.test_float)
    if x.sort_as != y.sort_as:
        return "GlossEntry {0} sort_as {2} != GlossEntry {1} sort_as {3}".format(x.id, y.id, x.sort_as, y.sort_as)
    if x.gloss_term != y.gloss_term:
        return "GlossEntry {0} gloss_term {2} != GlossEntry {1} gloss_term {3}".format(x.id, y.id, x.gloss_term, y.gloss_term)
    if x.acronym != y.acronym:
        return "GlossEntry {0} acronym {2} != GlossEntry {1} acronym {3}".format(x.id, y.id, x.acronym, y.acronym)
    if x.abbrev != y.abbrev:
        return "GlossEntry {0} abbrev {2} != GlossEntry {1} abbrev {3}".format(x.id, y.id, x.abbrev, y.abbrev)
    if x.gloss_see != y.gloss_see:
        return "GlossEntry {0} gloss_see {2} != GlossEntry {1} gloss_see {3}".format(x.id, y.id, x.gloss_see, y.gloss_see)
    return compare(x.gloss_def, y.gloss_def)


def compare_gloss_def(x, y, context):
    """
    :type x: GlossDef
    :type y: GlossDef
    """
    if x.para != y.para:
        return "GlossDef para {0} != GlossDef para {1}".format(x.para, y.para)
    return compare(x.gloss_see_also, y.gloss_see_also)

register(Glossary, compare_glossary)
register(GlossDiv, compare_gloss_div)
register(GlossList, compare_gloss_list)
register(GlossEntry, compare_gloss_entry)
register(GlossDef, compare_gloss_def)

class GlossaryTestSetup():
    class LoadedTestGlossaryHasExpectedEmptyValues:
        @staticmethod
        def glossary():
            return Glossary()

    class LoadedTestGlossaryWithMissingValues:
        @staticmethod
        def glossary():
            tempGlossary = Glossary()
            tempGlossDiv = GlossDiv()
            tempGlossList = GlossList()
            tempGlossEntry = GlossEntry()
            tempGlossDef = GlossDef()

            tempGlossEntry.gloss_def = tempGlossDef
            tempGlossList.gloss_entry = tempGlossEntry
            tempGlossDiv.gloss_list = tempGlossList
            tempGlossary.gloss_div = tempGlossDiv

            return tempGlossary