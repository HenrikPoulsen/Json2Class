from Generated.glossary import Glossary
from Generated.glossdiv import GlossDiv
from Generated.glossentry import GlossEntry
from Generated.glosslist import GlossList


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

            tempGlossList.glossEntry = tempGlossEntry
            tempGlossDiv.glossList = tempGlossList
            tempGlossary.glossDiv = tempGlossDiv

            return tempGlossary