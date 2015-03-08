package Generated;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import java.util.List;
import java.util.ArrayList;
import org.json.simple.JSONArray;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/***********************************************************************************/

public class GlossDiv{
    public GlossDiv() {
        title = "";
    }
    public String title;
    public GlossList glossList;

    public static class JsonSimpleFactory
    {
        public static String toJson(GlossDiv obj) {
            JSONObject json = toJsonObject(obj);
            return json.toString();
        }

        public static String toJson(List<GlossDiv> list) {
            JSONArray array = new JSONArray();
            for(GlossDiv obj : list)
            {
                array.add(toJsonObject(obj));
            }
            return array.toString();
        }

        public static JSONObject toJsonObject(GlossDiv obj) {
            JSONObject json = new JSONObject();
            json.put("title", obj.title);
            json.put("glossList", obj.glossList == null ? null : GlossList.JsonSimpleFactory.toJsonObject(obj.glossList));
            return json;
        }
        public static GlossDiv fromJson(String jsonString) {
            JSONObject jsonObject = (JSONObject)JSONValue.parse(jsonString);
            return fromJsonObject(jsonObject);
        }

        public static List<GlossDiv> fromJsonArray(String jsonArrayString) {
            JSONArray jsonArray = (JSONArray)JSONValue.parse(jsonArrayString);
            List<GlossDiv> result = new ArrayList<GlossDiv>();
            for(Object jsonObject : jsonArray)
            {
                result.add(fromJsonObject((JSONObject)jsonObject));
            }
            return result;
        }

        public static GlossDiv fromJsonObject(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            GlossDiv obj = new GlossDiv();
            if(jsonObject.containsKey("title")) {
                obj.title = (String)jsonObject.get("title");
            }
            obj.glossList = !jsonObject.containsKey("glossList") ? null : GlossList.JsonSimpleFactory.fromJsonObject((JSONObject)jsonObject.get("glossList"));
            return obj;
        }
    }
}
