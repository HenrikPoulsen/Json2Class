import Generated.GlossDef;
import Generated.Glossary;
import Generated.Person;
import junit.framework.TestCase;
import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

import java.util.ArrayList;

import static org.unitils.reflectionassert.ReflectionAssert.assertReflectionEquals;


public class JsonSimpleTest extends TestCase {
    public void testLoadedPersonHasExpectedName()
    {
        // Assemble
        String json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedName.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedName.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedAge()
    {
        // Assemble
        String json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedAge.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedCountry()
    {
        // Assemble
        String json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedCountry.Person(), loadedPerson);
    }

    public void testLoadedPersonHasExpectedFamily()
    {
        // Assemble

        String json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person());

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasExpectedFamily.Person(), loadedPerson);
    }

    public void testLoadedPersonWithMissingValues()
    {
        String json = Person.JsonSimpleFactory.toJson(PersonTestSetup.LoadedTestPersonWithMissingValues.Person());
        JSONObject jsonObject = (JSONObject)JSONValue.parse(json);
        jsonObject.remove("age");
        jsonObject.remove("family");

        // Act
        Person loadedPerson = Person.JsonSimpleFactory.fromJson(jsonObject.toString());

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonWithMissingValues.Person(), loadedPerson);
    }

    public void testLoadedPersonHasNullFamily()
    {
        Person person = PersonTestSetup.LoadedTestPersonHasNullFamily.Person();
        person.family = null;
        String json = Person.JsonSimpleFactory.toJson(person);

        // Act
        Person loadedGlossary = Person.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(PersonTestSetup.LoadedTestPersonHasNullFamily.Person(), loadedGlossary);
    }

    public void testLoadedGlossaryHasExpectedEmptyValues()
    {
        String json = Glossary.JsonSimpleFactory.toJson(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary());

        // Act
        Glossary loadedGlossary = Glossary.JsonSimpleFactory.fromJson(json);

        // Assert
        assertReflectionEquals(GlossaryTestSetup.LoadedTestGlossaryHasExpectedEmptyValues.Glossary(), loadedGlossary);
    }

    public void testLoadedGlossaryWithMissingValues()
    {
        String json = Glossary.JsonSimpleFactory.toJson(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary());
        JSONObject jsonObject = (JSONObject)JSONValue.parse(json);
        jsonObject.remove("title");
        ((JSONObject)jsonObject.get("glossDiv")).remove("title");
        ((JSONObject)((JSONObject)((JSONObject)jsonObject.get("glossDiv")).get("glossList")).get("glossEntry")).remove("id");
        ((JSONObject)((JSONObject)((JSONObject)jsonObject.get("glossDiv")).get("glossList")).get("glossEntry")).remove("float");

        // Act
        Glossary loadedGlossary = Glossary.JsonSimpleFactory.fromJson(jsonObject.toString());

        // Assert
        assertReflectionEquals(GlossaryTestSetup.LoadedTestGlossaryWithMissingValues.Glossary(), loadedGlossary);
    }
}
