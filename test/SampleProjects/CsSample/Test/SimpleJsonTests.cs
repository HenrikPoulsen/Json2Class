using System;
using System.Collections.Generic;
using ExpectedObjects;
using Generated;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
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
            var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedName.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedAge()
        {
            // Assemble
            var jsonString = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(jsonString);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedAge.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedCountry()
        {
            // Assemble
            var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person());

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonHasExpectedFamily()
        {
            // Assemble
            
            var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person());

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person().ToExpectedObject().ShouldMatch(loadedPerson);
        }

        [TestMethod]
        public void LoadedTestPersonWithMissingValues()
        {
            var jsonString = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
            var jsonObject = JSON.Parse(jsonString);
            jsonObject.Remove("age");
            jsonObject.Remove("family");

            // Act
            var loadedGlossary = Person.SimpleJsonFactory.FromJson(jsonObject.ToString());

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
            var json = Person.SimpleJsonFactory.ToJson(person);

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(json);

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
            var json = Glossary.SimpleJsonFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary());

            // Act
            var loadedGlossary = Glossary.SimpleJsonFactory.FromJson(json);

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }

        [TestMethod]
        public void LoadedTestGlossaryWithMissingValues()
        {
            var jsonString = Glossary.SimpleJsonFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
            var jsonObject = JSON.Parse(jsonString);
            jsonObject.Remove("title");
            jsonObject["glossDiv"].Remove("title");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("id");
            jsonObject["glossDiv"]["glossList"]["glossEntry"].Remove("float");

            // Act
            var loadedGlossary = Glossary.SimpleJsonFactory.FromJson(jsonObject.ToString());

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }
        #endregion
    }
}
