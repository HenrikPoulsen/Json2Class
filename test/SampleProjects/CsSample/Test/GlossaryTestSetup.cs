using Generated;

namespace Test
{
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
                return new Glossary()
                {
                    GlossDiv = new GlossDiv { GlossList = new GlossList { GlossEntry = new GlossEntry() } }
                };
            }
        }
    }
}
