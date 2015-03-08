import Generated.Gender;
import Generated.Person;

import java.util.ArrayList;
import java.util.List;

class PersonTestSetup
{
    public static class LoadedTestPersonHasExpectedName
    {
        public static Person Person()
        {
            Person temp = new Person();
            temp.name = "Hello";
            return temp;
        }
    }

    public static class LoadedTestPersonHasExpectedAge
    {
        public static Person Person()
        {
            Person temp = new Person();
            temp.age = Long.valueOf(100);
            return temp;
        }
    }

    public static class LoadedTestPersonHasExpectedCountry
    {
        public static Person Person()
        {
            Person temp = new Person();
            temp.country = "ExpectedCountry";
            return temp;
        }
    }

    public static class LoadedTestPersonHasExpectedFamily
    {
        public static Person Person()
        {
            Person temp = new Person();
            temp.name = "empty";
            temp.age = Long.valueOf(10);
            temp.gender = Gender.MALE;
            temp.country = "Whatever";
            temp.family = new ArrayList<Person>();
            temp.family.add(new Person());
            temp.family.get(0).name = "Family";
            temp.family.get(0).gender = Gender.FEMALE;
            temp.family.get(0).age = Long.valueOf(-1);
            temp.family.get(0).country = "Random";
            temp.family.add(new Person());
            return temp;
        }
    }

    public static class LoadedTestPersonHasNullFamily
    {
        public static Person Person()
        {
            Person temp = new Person();
            temp.name = "Empty";
            temp.age = Long.valueOf(10);
            temp.country = "Whatever";
            temp.family = new ArrayList<Person>();
            return temp;
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
            List<Person> people = new ArrayList<Person>();
            people.add(new Person());
            people.add(new Person());
            people.get(0).age = 3L;
            people.get(0).country = "DK";
            people.get(0).isHuman = true;
            people.get(0).name = "Olle";

            people.get(1).age = 187L;
            people.get(1).country = "NA";
            people.get(1).isHuman = false;
            people.get(1).name = "Splork";
            return people;
        }

    }
}
