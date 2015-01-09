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
            temp.age = 100;
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
            temp.age = 10;
            temp.country = "Whatever";
            temp.family = new ArrayList<Person>();
            temp.family.add(new Person());
            temp.family.get(0).name = "Family";
            temp.family.get(0).age = -1;
            temp.family.get(0).country = "Random";
            temp.family.add(new Person());
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
}
