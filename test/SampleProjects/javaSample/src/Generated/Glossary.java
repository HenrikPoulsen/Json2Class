package Generated;

import org.json.simple.JSONObject;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-07                                                                */
/***********************************************************************************/

public class Glossary{
    public Glossary() {
        title = "";
    }
    public Glossary(JSONObject jsonObject) {
        title = (String)jsonObject.get("title");
        glossDiv = new GlossDiv((JSONObject)jsonObject.get("glossDiv"));
    }

    public String title;
    public GlossDiv glossDiv;

    public JSONObject toJson() {
        JSONObject json = new JSONObject();
        json.put("title", title);
        json.put("glossDiv", glossDiv.toJson());
        return json;
    }
}
