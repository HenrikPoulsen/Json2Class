package Generated;

import org.json.simple.JSONObject;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-09                                                                */
/***********************************************************************************/

public class Minimal{
    public Minimal() {
    }

    public static class JsonSimpleFactory
    {
        public static JSONObject toJson(Minimal obj) {
            JSONObject json = new JSONObject();
            return json;
        }
        public static Minimal fromJson(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            Minimal obj = new Minimal();
            return obj;
        }
    }
}