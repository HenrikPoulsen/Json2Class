using SimpleJSON;
using System.Collections.Generic;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class ObjectList
    {
        public ObjectList()
        {
            Name = string.Empty;
        }

        public string Name {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(ObjectList obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(ObjectList obj)
            {
                var jsonObject = new JSONClass();
                if (obj.Name != null)
                    jsonObject["name"] = new JSONData(obj.Name);
                return jsonObject;
            }

            public static ObjectList FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static ObjectList FromJsonObject(JSONNode jsonObject)
            {
                var name = jsonObject["name"].Value ?? "";
                return new ObjectList
                {
                    Name = name,
                };
            }

        }

        public static class FastJSONFactory
        {
            public static string ToJson(ObjectList obj)
            {
                var jsonObject = ToJsonObject(obj);
                return fastJSON.JSON.ToJSON(jsonObject);
            }

            public static Dictionary<string, object> ToJsonObject(ObjectList obj)
            {
                var jsonObject = new Dictionary<string, object>();
                if (obj.Name != null)
                    jsonObject["name"] = obj.Name;
                return jsonObject;
            }

            public static ObjectList FromJson(string jsonString)
            {
                var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static ObjectList FromJsonObject(Dictionary<string, object> jsonObject)
            {
                var name = jsonObject.ContainsKey("name") ? jsonObject["name"] as string : "";
                return new ObjectList
                {
                    Name = name,
                };
            }

        }
    }
}
