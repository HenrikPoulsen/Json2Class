import Generated.GlossDiv;
import Generated.GlossEntry;
import Generated.GlossList;
import Generated.Glossary;

class GlossaryTestSetup
{
    public static class LoadedTestGlossaryHasExpectedEmptyValues
    {
        public static Glossary Glossary()
        {
            return new Glossary();
        }
    }

    public static class LoadedTestGlossaryWithMissingValues
    {
        public static Glossary Glossary()
        {
            Glossary tempGlossary = new Glossary();
            GlossDiv tempGlossDiv = new GlossDiv();
            GlossList tempGlossList = new GlossList();
            GlossEntry tempGlossEntry = new GlossEntry();

            tempGlossList.glossEntry = tempGlossEntry;
            tempGlossDiv.glossList = tempGlossList;
            tempGlossary.glossDiv = tempGlossDiv;

            return tempGlossary;
        }
    }
}