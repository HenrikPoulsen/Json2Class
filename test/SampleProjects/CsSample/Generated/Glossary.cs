using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-04                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class Glossary
    {
        public Glossary()
        {
            Title = string.Empty;
        }

        public Glossary(JSONNode jsonObject)
        {
            Title = jsonObject["title"];
            GlossDiv = new GlossDiv(jsonObject["glossDiv"]);
        }

        public string Title {get; set;}
        public GlossDiv GlossDiv {get; set;}

        public JSONNode ToJson()
        {
            var json = new JSONClass();
            json["title"] = new JSONData(Title);
            json["glossDiv"] = GlossDiv.ToJson();
            return json;
        }
    }
}
