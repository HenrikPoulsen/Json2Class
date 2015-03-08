using SimpleJSON;
using System.Collections.Generic;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossDiv
    {
        public GlossDiv()
        {
            Title = string.Empty;
        }

        public string Title {get; set;}
        public GlossList GlossList {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(GlossDiv obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static string ToJson(List<GlossDiv> arr)
            {
                var array = new JSONArray();
                foreach (var item in arr)
                {
                    array.Add(ToJsonObject(item));
                }
                return array.ToString();
            }

            public static JSONNode ToJsonObject(GlossDiv obj)
            {
                var jsonObject = new JSONClass();
                if (obj.Title != null)
                    jsonObject["title"] = new JSONData(obj.Title);
                if (obj.GlossList != null)
                    jsonObject["glossList"] = Generated.GlossList.SimpleJsonFactory.ToJsonObject(obj.GlossList);
                return jsonObject;
            }

            public static GlossDiv FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static List<GlossDiv> FromJsonArray(string jsonArrayString)
            {
                var jsonArray = JSON.Parse(jsonArrayString);
                var result = new List<GlossDiv>();
                foreach (JSONNode jsonObject in jsonArray.AsArray)
                {
                    result.Add(FromJsonObject(jsonObject));
                }
                return result;
            }

            public static GlossDiv FromJsonObject(JSONNode jsonObject)
            {
                var title = jsonObject["title"].Value ?? "";
                var glossList = jsonObject["glossList"] != null ? Generated.GlossList.SimpleJsonFactory.FromJsonObject(jsonObject["glossList"]) : null;
                return new GlossDiv
                {
                    Title = title,
                    GlossList = glossList,
                };
            }

        }
    }
}
