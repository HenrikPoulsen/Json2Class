using System.Collections.Generic;
using SimpleJSON;
using System.Collections.Generic;

/////////////////////////////////////////////////////////////////////////////////////
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-01-12                                                                */
/////////////////////////////////////////////////////////////////////////////////////

namespace Generated
{
    public class Person
    {
        public Person()
        {
            Name = string.Empty;
            Country = string.Empty;
            Family = new List<Person>();
        }

        public string Name {get; set;}
        public long Age {get; set;}
        public string Country {get; set;}
        public bool IsHuman {get; set;}
        public List<Person> Family {get; set;}

        public static class SimpleJsonFactory
        {
            public static string ToJson(Person obj)
            {
                var jsonObject = ToJsonObject(obj);
                return jsonObject.ToString();
            }

            public static JSONNode ToJsonObject(Person obj)
            {
                var jsonObject = new JSONClass();
                if (obj.Name != null)
                    jsonObject["name"] = new JSONData(obj.Name);
                jsonObject["age"] = new JSONData(obj.Age);
                if (obj.Country != null)
                    jsonObject["country"] = new JSONData(obj.Country);
                jsonObject["isHuman"] = new JSONData(obj.IsHuman);
                if(obj.Family != null)
                {
                    var family = new JSONArray();
                    foreach(var item in obj.Family)
                    {
                        family.Add(Generated.Person.SimpleJsonFactory.ToJsonObject(item));
                    }
                    jsonObject["family"] = family;
                }
                return jsonObject;
            }

            public static Person FromJson(string jsonString)
            {
                var jsonObject = JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static Person FromJsonObject(JSONNode jsonObject)
            {
                var name = jsonObject["name"].Value ?? "";
                var age = jsonObject["age"].AsInt;
                var country = jsonObject["country"].Value ?? "";
                var isHuman = jsonObject["isHuman"].AsBool;
                var family = new List<Person>();
                foreach(JSONNode item in jsonObject["family"].AsArray)
                {
                    family.Add(Generated.Person.SimpleJsonFactory.FromJsonObject(item));
                }

                return new Person
                {
                    Name = name,
                    Age = age,
                    Country = country,
                    IsHuman = isHuman,
                    Family = family,
                };
            }

        }

        public static class FastJSONFactory
        {
            public static string ToJson(Person obj)
            {
                var jsonObject = ToJsonObject(obj);
                return fastJSON.JSON.ToJSON(jsonObject);
            }

            public static Dictionary<string, object> ToJsonObject(Person obj)
            {
                var jsonObject = new Dictionary<string, object>();
                if (obj.Name != null)
                    jsonObject["name"] = obj.Name;
                jsonObject["age"] = obj.Age;
                if (obj.Country != null)
                    jsonObject["country"] = obj.Country;
                jsonObject["isHuman"] = obj.IsHuman;
                if(obj.Family != null)
                {
                    var family = new List<Dictionary<string,object>>();
                    foreach(var item in obj.Family)
                    {
                        family.Add(Generated.Person.FastJSONFactory.ToJsonObject(item));
                    }
                    jsonObject["family"] = family;
                }
                return jsonObject;
            }

            public static Person FromJson(string jsonString)
            {
                var jsonObject = (Dictionary<string, object>)fastJSON.JSON.Parse(jsonString);
                return FromJsonObject(jsonObject);
            }

            public static Person FromJsonObject(Dictionary<string, object> jsonObject)
            {
                var name = jsonObject.ContainsKey("name") ? jsonObject["name"] as string : "";
                var age = jsonObject.ContainsKey("age") ? (long)jsonObject["age"] : 0;
                var country = jsonObject.ContainsKey("country") ? jsonObject["country"] as string : "";
                var isHuman = jsonObject.ContainsKey("isHuman") ? (bool)jsonObject["isHuman"] : false;
                var family = new List<Person>();
                if(jsonObject.ContainsKey("family"))
                {
                    foreach(Dictionary<string,object> item in jsonObject["family"] as List<object>)
                    {
                        family.Add(Generated.Person.FastJSONFactory.FromJsonObject(item));
                    }
                }

                return new Person
                {
                    Name = name,
                    Age = age,
                    Country = country,
                    IsHuman = isHuman,
                    Family = family,
                };
            }

        }
    }
}
