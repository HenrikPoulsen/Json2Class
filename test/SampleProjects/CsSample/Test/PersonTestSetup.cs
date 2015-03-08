using System.Collections.Generic;
using Generated;

namespace Test
{
    class PersonTestSetup
    {
        public static class LoadedTestPersonHasExpectedName
        {
            public static Person Person()
            {
                return new Person
                {
                    Name = "Hello"
                };
            }
        }

        public static class LoadedTestPersonHasExpectedAge
        {
            public static Person Person()
            {
                return new Person
                {
                    Age = 100
                };
            }
        }

        public static class LoadedTestPersonHasExpectedCountry
        {
            public static Person Person()
            {
                return new Person
                {
                    Country = "ExpectedCountry"
                };
            }
        }

        public static class LoadedTestPersonHasExpectedFamily
        {
            public static Person Person()
            {
                return new Person
                {
                    Name = "Empty",
                    Age = 10,
                    Country = "Whatever",
                    Family = new List<Person>
                    {
                        new Person
                        {
                            Name = "Family",
                            Age = -1,
                            Country = "Random"

                        },
                        new Person()
                    }
                };
            }
        }

        public static class LoadedTestPersonHasNullFamily
        {
            public static Person Person()
            {
                return new Person
                {
                    Name = "Empty",
                    Age = 10,
                    Country = "Whatever",
                    Family = new List<Person>()
                };
            }
        }

        public static class LoadedTestPersonWithMissingValues
        {
            public static Person Person()
            {
                return new Person();
            }
        }

        public static class LoadedTestPersonListAsExpected
        {
            public static List<Person> People()
            {
                return new List<Person>
                {
                    new Person
                    {
                        Age = 3,
                        Country = "DK",
                        IsHuman = true,
                        Name = "Olle"
                    },
                    new Person
                    {
                        Age = 187,
                        Country = "NA",
                        IsHuman = false,
                        Name = "Splork"
                    }
                };
            }
        }
    }
}
