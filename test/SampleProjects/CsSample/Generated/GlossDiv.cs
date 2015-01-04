using SimpleJSON;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-04                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossDiv
    {
        public GlossDiv()
        {
            Title = string.Empty;
        }

        public GlossDiv(JSONNode jsonObject)
        {
            Title = jsonObject["title"];
            GlossList = new GlossList(jsonObject["glossList"]);
        }

        public string Title {get; set;}
        public GlossList GlossList {get; set;}

        public JSONNode ToJson()
        {
            var json = new JSONClass();
            json["title"] = new JSONData(Title);
            json["glossList"] = GlossList.ToJson();
            return json;
        }
    }
}
