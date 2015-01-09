import Generated.GlossDef;
import Generated.Glossary;
import Generated.Person;
import junit.framework.TestCase;
import org.json.simple.JSONObject;

import java.util.ArrayList;

import static org.unitils.reflectionassert.ReflectionAssert.assertReflectionEquals;


public class JsonSimpleTest extends TestCase {
    public void testLoadedPersonHasExpectedName()
    {
        // Assemble
        JSONObject json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedName.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedAge()
    {
        // Assemble
        JSONObject json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedCountry()
    {
        // Assemble
        JSONObject json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedFamily()
    {
        // Assemble

        JSONObject json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person(), loadedPerson);
    }

    public void testLoadedPersonWithMissingValues()
    {
        JSONObject json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
        json.remove("age");
        json.remove("family");

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonWithMissingValues.Person(), loadedPerson);
    }

    public void testLoadedGlossaryHasExpectedEmptyValues()
    {
        JSONObject json = Glossary.JsonSimpleFactory.toJson(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary());

        // Act
        Glossary loadedGlossary = Glossary.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary(), loadedGlossary);
    }

    public void testLoadedGlossaryWithMissingValues()
    {
        JSONObject json = Glossary.JsonSimpleFactory.toJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
        json.remove("title");
        ((JSONObject)json.get("glossDiv")).remove("title");
        ((JSONObject)((JSONObject)((JSONObject)json.get("glossDiv")).get("glossList")).get("glossEntry")).remove("id");
        ((JSONObject)((JSONObject)((JSONObject)json.get("glossDiv")).get("glossList")).get("glossEntry")).remove("float");

        // Act
        Glossary loadedGlossary = Glossary.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary(), loadedGlossary);
    }
}
