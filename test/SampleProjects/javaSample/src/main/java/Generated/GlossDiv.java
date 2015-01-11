package Generated;

import org.json.simple.JSONObject;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-11                                                                */
/***********************************************************************************/

public class GlossDiv{
    public GlossDiv() {
        title = "";
    }
    public String title;
    public GlossList glossList;

    public static class JsonSimpleFactory
    {
        public static JSONObject toJson(GlossDiv obj) {
            JSONObject json = new JSONObject();
            json.put("title", obj.title);
            json.put("glossList", obj.glossList == null ? null : GlossList.JsonSimpleFactory.toJson(obj.glossList));
            return json;
        }
        public static GlossDiv fromJson(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            GlossDiv obj = new GlossDiv();
            if(jsonObject.containsKey("title")) {
                obj.title = (String)jsonObject.get("title");
            }
            obj.glossList = !jsonObject.containsKey("glossList") ? null : GlossList.JsonSimpleFactory.fromJson((JSONObject)jsonObject.get("glossList"));
            return obj;
        }
    }
}
