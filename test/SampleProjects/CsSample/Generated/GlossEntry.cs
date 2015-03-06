using SimpleJSON;
using System.Collections.Generic;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class GlossEntry
    {
        public GlossEntry()
        {
            SortAs = string.Empty;
            GlossTerm = string.Empty;
            Acronym = string.Empty;
            Abbrev = string.Empty;
            GlossSee = string.Empty;
        }

        public long Id {get; set;}
        public float TestFloat {get; set;}
        public string SortAs {get; set;}
        public string GlossTerm {get; set;}
        public string Acronym {get; set;}
        public string Abbrev {get; set;}
        public GlossDef GlossDef {get; set;}
        public string GlossSee {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(GlossEntry obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(GlossEntry obj)
            {
                var jsonObject = new JSONClass();
                jsonObject["id"] = new JSONData(obj.Id);
                jsonObject["testFloat"] = new JSONData(obj.TestFloat);
                if (obj.SortAs != null)
                    jsonObject["sortAs"] = new JSONData(obj.SortAs);
                if (obj.GlossTerm != null)
                    jsonObject["glossTerm"] = new JSONData(obj.GlossTerm);
                if (obj.Acronym != null)
                    jsonObject["acronym"] = new JSONData(obj.Acronym);
                if (obj.Abbrev != null)
                    jsonObject["abbrev"] = new JSONData(obj.Abbrev);
                if (obj.GlossDef != null)
                    jsonObject["glossDef"] = Generated.GlossDef.SimpleJsonFactory.ToJsonObject(obj.GlossDef);
                if (obj.GlossSee != null)
                    jsonObject["glossSee"] = new JSONData(obj.GlossSee);
                return jsonObject;
            }

            public static GlossEntry FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static GlossEntry FromJsonObject(JSONNode jsonObject)
            {
                var id = jsonObject["id"].AsInt;
                var testFloat = jsonObject["testFloat"].AsFloat;
                var sortAs = jsonObject["sortAs"].Value ?? "";
                var glossTerm = jsonObject["glossTerm"].Value ?? "";
                var acronym = jsonObject["acronym"].Value ?? "";
                var abbrev = jsonObject["abbrev"].Value ?? "";
                var glossDef = jsonObject["glossDef"] != null ? Generated.GlossDef.SimpleJsonFactory.FromJsonObject(jsonObject["glossDef"]) : null;
                var glossSee = jsonObject["glossSee"].Value ?? "";
                return new GlossEntry
                {
                    Id = id,
                    TestFloat = testFloat,
                    SortAs = sortAs,
                    GlossTerm = glossTerm,
                    Acronym = acronym,
                    Abbrev = abbrev,
                    GlossDef = glossDef,
                    GlossSee = glossSee,
                };
            }

        }

        public static class FastJSONFactory
        {
            public static string ToJson(GlossEntry obj)
            {
                var jsonObject = ToJsonObject(obj);
                return fastJSON.JSON.ToJSON(jsonObject);
            }

            public static Dictionary<string, object> ToJsonObject(GlossEntry obj)
            {
                var jsonObject = new Dictionary<string, object>();
                jsonObject["id"] = obj.Id;
                jsonObject["testFloat"] = obj.TestFloat;
                if (obj.SortAs != null)
                    jsonObject["sortAs"] = obj.SortAs;
                if (obj.GlossTerm != null)
                    jsonObject["glossTerm"] = obj.GlossTerm;
                if (obj.Acronym != null)
                    jsonObject["acronym"] = obj.Acronym;
                if (obj.Abbrev != null)
                    jsonObject["abbrev"] = obj.Abbrev;
                if (obj.GlossDef != null)
                    jsonObject["glossDef"] = Generated.GlossDef.FastJSONFactory.ToJsonObject(obj.GlossDef);
                if (obj.GlossSee != null)
                    jsonObject["glossSee"] = obj.GlossSee;
                return jsonObject;
            }

            public static GlossEntry FromJson(string jsonString)
            {
                var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static GlossEntry FromJsonObject(Dictionary<string, object> jsonObject)
            {
                var id = jsonObject.ContainsKey("id") ? (long)jsonObject["id"] : 0;
                var testFloat = jsonObject.ContainsKey("testFloat") ? float.Parse(jsonObject["testFloat"] as string) : 0.0f;
                var sortAs = jsonObject.ContainsKey("sortAs") ? jsonObject["sortAs"] as string : "";
                var glossTerm = jsonObject.ContainsKey("glossTerm") ? jsonObject["glossTerm"] as string : "";
                var acronym = jsonObject.ContainsKey("acronym") ? jsonObject["acronym"] as string : "";
                var abbrev = jsonObject.ContainsKey("abbrev") ? jsonObject["abbrev"] as string : "";
                var glossDef = jsonObject.ContainsKey("glossDef") ? Generated.GlossDef.FastJSONFactory.FromJsonObject(jsonObject["glossDef"] as Dictionary<string, object>) : null;
                var glossSee = jsonObject.ContainsKey("glossSee") ? jsonObject["glossSee"] as string : "";
                return new GlossEntry
                {
                    Id = id,
                    TestFloat = testFloat,
                    SortAs = sortAs,
                    GlossTerm = glossTerm,
                    Acronym = acronym,
                    Abbrev = abbrev,
                    GlossDef = glossDef,
                    GlossSee = glossSee,
                };
            }

        }
    }
}
