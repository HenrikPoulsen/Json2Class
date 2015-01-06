using System;
using System.Collections.Generic;
using ExpectedObjects;
using Generated;
using Microsoft.VisualStudio.TestTools.UnitTesting;

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
            var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

            // Act
            var loadedPerson = Person.SimpleJsonFactory.FromJson(json);

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
            var json = Person.SimpleJsonFactory.ToJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
            json.Remove("age");
            json.Remove("family");

            // Act
            var loadedGlossary = Person.SimpleJsonFactory.FromJson(json);

            // Assert
            PersonTestSetup.LoadedTestPersonWithMissingValues.Person()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
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
            var json = Glossary.SimpleJsonFactory.ToJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
            json.Remove("title");
            json["glossDiv"].Remove("title");
            json["glossDiv"]["glossList"]["glossEntry"].Remove("id");
            json["glossDiv"]["glossList"]["glossEntry"].Remove("float");

            // Act
            var loadedGlossary = Glossary.SimpleJsonFactory.FromJson(json);

            // Assert
            GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary()
                .ToExpectedObject()
                .ShouldMatch(loadedGlossary);
        }
        #endregion
    }
}
