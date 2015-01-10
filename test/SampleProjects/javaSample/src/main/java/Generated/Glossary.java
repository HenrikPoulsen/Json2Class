package Generated;

import org.json.simple.JSONObject;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-10                                                                */
/***********************************************************************************/

public class Glossary{
    public Glossary() {
        title = "";
    }
    public String title;
    public GlossDiv glossDiv;

    public static class JsonSimpleFactory
    {
        public static JSONObject toJson(Glossary obj) {
            JSONObject json = new JSONObject();
            json.put("title", obj.title);
            json.put("glossDiv", obj.glossDiv == null ? null : GlossDiv.JsonSimpleFactory.toJson(obj.glossDiv));
            return json;
        }
        public static Glossary fromJson(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            Glossary obj = new Glossary();
            if(jsonObject.containsKey("title")) {
                obj.title = (String)jsonObject.get("title");
            }
            obj.glossDiv = !jsonObject.containsKey("glossDiv") ? null : GlossDiv.JsonSimpleFactory.fromJson((JSONObject)jsonObject.get("glossDiv"));
            return obj;
        }
    }
}
