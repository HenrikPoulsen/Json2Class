using System;
using System.Diagnostics;
using ExpectedObjects;
using Generated;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using SimpleJSON;

namespace Test
{
    [TestClass]
    public class SimpleJsonTests
    {
        #region Person Tests

        [TestMethod]
        public void LoadedTestPersonHasExpectedName()
        {
            // Assemble
            string json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());

            // Act
            Person loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedName.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedAge()
        {
            // Assemble
            string jsonString = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

            // Act
            Person loadedPerson = Person.SimpleJsonFactory.FromJson(jsonString);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedAge.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedCountry()
        {
            // Assemble
            string json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person());

            // Act
            Person loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedFamily()
        {
            // Assemble

            string json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person());

            // Act
            Person loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonWithMissingValues()
        {
            string jsonString =
                Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
            JSONNode jsonObject = JSON.Parse(jsonString);
            jsonObject.Remove("age");
            jsonObject.Remove("family");

            // Act
            Person loadedGlossary = Person.SimpleJsonFactory.FromJson(jsonObject.ToString());

            // Assert
            PersonTestSetup.LoadedTestPersonWithMissingValues.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        [TestMethod]
        public void LoadedTestPersonHasNullFamily()
        {
            Person person = PersonTestSetup.LoadedTestPersonHasNullFamily.Person();
            person.Family = null;
            string json = Person.SimpleJsonFactory.ToJson(person);

            // Act
            Person loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasNullFamily.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonListAsExpected()
        {
            var people = PersonTestSetup.LoadedTestPersonListAsExpected.People();
            string json = Person.SimpleJsonFactory.ToJson(people);

            // Act
            var loadedPeople = Person.SimpleJsonFactory.FromJsonArray(json);

            // Assert
            PersonTestSetup.LoadedTestPersonListAsExpected.People()
                .ToExpectedObject()
                .ShouldMatch(loadedPeople);
        }

        #endregion

        #region Glossary Tests

        [TestMethod]
        public void LoadedTestGlossaryHasExpectedEmptyValues()
        {
            string json =
                Glossary.SimpleJsonFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary());

            // Act
            Glossary loadedGlossary = Glossary.SimpleJsonFactory.FromJson(json);

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        [TestMethod]
        public void LoadedTestGlossaryWithMissingValues()
        {
            string jsonString =
                Glossary.SimpleJsonFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
            JSONNode jsonObject = JSON.Parse(jsonString);
            jsonObject.Remove("title");
            jsonObject["glossDiv"].Remove("title");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("id");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("float");

            // Act
            Glossary loadedGlossary = Glossary.SimpleJsonFactory.FromJson(jsonObject.ToString());

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        #endregion

        [TestMethod]
        public void PerformanceTest()
        {
            var sw = new Stopwatch();

            sw.Start();

            var remaining = 10000;

            while (remaining != 0)
            {
                var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());
                Person.SimpleJsonFactory.FromJson(json);
                remaining--;
            }

            sw.Stop();

            Console.WriteLine("Elapsed={0}", sw.Elapsed);

        }
    }
}