package Generated;

/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/***********************************************************************************/

public class Gender{
    public static Gender UNSPECIFIED = new Gender(0);
    public static Gender MALE = new Gender(1);
    public static Gender FEMALE = new Gender(2);

    private long value;
    public long getValue() { return value; }
    public Gender(long val) {
        value = val;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Gender gender = (Gender) o;

        return value == gender.value;
    }

    @Override
    public int hashCode() {
        return (int) (value ^ (value >>> 32));
    }
}