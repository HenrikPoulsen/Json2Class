using SimpleJSON;
using System.Collections.Generic;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class Glossary
    {
        public Glossary()
        {
            Title = string.Empty;
        }

        public string Title {get; set;}
        public GlossDiv GlossDiv {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(Glossary obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(Glossary obj)
            {
                var jsonObject = new JSONClass();
                if (obj.Title != null)
                    jsonObject["title"] = new JSONData(obj.Title);
                if (obj.GlossDiv != null)
                    jsonObject["glossDiv"] = Generated.GlossDiv.SimpleJsonFactory.ToJsonObject(obj.GlossDiv);
                return jsonObject;
            }

            public static Glossary FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static Glossary FromJsonObject(JSONNode jsonObject)
            {
                var title = jsonObject["title"].Value ?? "";
                var glossDiv = jsonObject["glossDiv"] != null ? Generated.GlossDiv.SimpleJsonFactory.FromJsonObject(jsonObject["glossDiv"]) : null;
                return new Glossary
                {
                    Title = title,
                    GlossDiv = glossDiv,
                };
            }

        }

        public static class FastJSONFactory
        {
            public static string ToJson(Glossary obj)
            {
                var jsonObject = ToJsonObject(obj);
                return fastJSON.JSON.ToJSON(jsonObject);
            }

            public static Dictionary<string, object> ToJsonObject(Glossary obj)
            {
                var jsonObject = new Dictionary<string, object>();
                if (obj.Title != null)
                    jsonObject["title"] = obj.Title;
                if (obj.GlossDiv != null)
                    jsonObject["glossDiv"] = Generated.GlossDiv.FastJSONFactory.ToJsonObject(obj.GlossDiv);
                return jsonObject;
            }

            public static Glossary FromJson(string jsonString)
            {
                var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static Glossary FromJsonObject(Dictionary<string, object> jsonObject)
            {
                var title = jsonObject.ContainsKey("title") ? jsonObject["title"] as string : "";
                var glossDiv = jsonObject.ContainsKey("glossDiv") ? Generated.GlossDiv.FastJSONFactory.FromJsonObject(jsonObject["glossDiv"] as Dictionary<string, object>) : null;
                return new Glossary
                {
                    Title = title,
                    GlossDiv = glossDiv,
                };
            }

        }
    }
}
