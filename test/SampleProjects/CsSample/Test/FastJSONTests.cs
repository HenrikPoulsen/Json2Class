using System;
using System.Collections.Generic;
using System.Diagnostics;
using ExpectedObjects;
using Generated;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
using SimpleJSON;

namespace Test
{
    [TestClass]
    public class FastJSONTests
    {
        #region Person Tests
        [TestMethod]
        public void LoadedTestPersonHasExpectedName()
        {
            // Assemble
            var json = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());

            // Act
            var loadedPerson = Person.FastJSONFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedName.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedAge()
        {
            // Assemble
            var jsonString = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

            // Act
            var loadedPerson = Person.FastJSONFactory.FromJson(jsonString);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedAge.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedCountry()
        {
            // Assemble
            var json = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person());

            // Act
            var loadedPerson = Person.FastJSONFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedFamily()
        {
            // Assemble

            var json = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person());

            // Act
            var loadedPerson = Person.FastJSONFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonWithMissingValues()
        {
            var jsonString = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
            var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);
            jsonObject.Remove("age");
            jsonObject.Remove("family");
            jsonString = fastJSON.JSON.ToJSON(jsonObject);

            // Act
            var loadedGlossary = Person.FastJSONFactory.FromJson(jsonString);

            // Assert
            PersonTestSetup.LoadedTestPersonWithMissingValues.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        [TestMethod]
        public void LoadedTestPersonHasNullFamily()
        {
            var person = PersonTestSetup.LoadedTestPersonHasNullFamily.Person();
            person.Family = null;
            var json = Person.FastJSONFactory.ToJson(person);

            // Act
            var loadedPerson = Person.FastJSONFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasNullFamily.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }
        #endregion

        #region Glossary Tests
        [TestMethod]
        public void LoadedTestGlossaryHasExpectedEmptyValues()
        {
            var json = Glossary.FastJSONFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary());

            // Act
            var loadedGlossary = Glossary.FastJSONFactory.FromJson(json);

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        [TestMethod]
        public void LoadedTestGlossaryWithMissingValues()
        {
            var jsonString = Glossary.FastJSONFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
            var jsonObject = JSON.Parse(jsonString);
            jsonObject.Remove("title");
            jsonObject["glossDiv"].Remove("title");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("id");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("float");

            // Act
            var loadedGlossary = Glossary.FastJSONFactory.FromJson(jsonObject.ToString());

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
                var json = Person.FastJSONFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());
                Person.FastJSONFactory.FromJson(json);
                remaining--;
            }

            sw.Stop();

            Console.WriteLine("Elapsed={0}",sw.Elapsed);
           
        }
    }
}
