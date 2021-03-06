package Generated;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import java.util.List;
import java.util.ArrayList;
import org.json.simple.JSONArray;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/*                                                                                 */
/***********************************************************************************/

public class ListSample{
    public ListSample() {
        intList = new ArrayList<Long>();
        floatList = new ArrayList<Float>();
        stringList = new ArrayList<String>();
        objectList = new ArrayList<ObjectList>();
    }
    public List<Long> intList;
    public List<Float> floatList;
    public List<String> stringList;
    public List<ObjectList> objectList;

    public static class JsonSimpleFactory
    {
        public static String toJson(ListSample obj) {
            JSONObject json = toJsonObject(obj);
            return json.toString();
        }

        public static String toJson(List<ListSample> list) {
            JSONArray array = new JSONArray();
            for(ListSample obj : list)
            {
                array.add(toJsonObject(obj));
            }
            return array.toString();
        }

        public static JSONObject toJsonObject(ListSample obj) {
            JSONObject json = new JSONObject();
            JSONArray tempArray;

            if(obj.intList != null) {
                tempArray = new JSONArray();
                for(Long item : obj.intList){
                    tempArray.add(item);
                }
                json.put("intList", tempArray);
            }

            if(obj.floatList != null) {
                tempArray = new JSONArray();
                for(Float item : obj.floatList){
                    tempArray.add(item);
                }
                json.put("floatList", tempArray);
            }

            if(obj.stringList != null) {
                tempArray = new JSONArray();
                for(String item : obj.stringList){
                    tempArray.add(item);
                }
                json.put("stringList", tempArray);
            }

            if(obj.objectList != null) {
                tempArray = new JSONArray();
                for(ObjectList item : obj.objectList){
                    tempArray.add(ObjectList.JsonSimpleFactory.toJsonObject(item));
                }
                json.put("objectList", tempArray);
            }
            return json;
        }
        public static ListSample fromJson(String jsonString) {
            JSONObject jsonObject = (JSONObject)JSONValue.parse(jsonString);
            return fromJsonObject(jsonObject);
        }

        public static List<ListSample> fromJsonArray(String jsonArrayString) {
            JSONArray jsonArray = (JSONArray)JSONValue.parse(jsonArrayString);
            List<ListSample> result = new ArrayList<ListSample>();
            for(Object jsonObject : jsonArray)
            {
                result.add(fromJsonObject((JSONObject)jsonObject));
            }
            return result;
        }

        public static ListSample fromJsonObject(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            ListSample obj = new ListSample();
            if(jsonObject.containsKey("intList")) {
                obj.intList = new ArrayList<Long>();
                for(Object item : (JSONArray)jsonObject.get("intList")) {
                    obj.intList.add((Long)item);
                }
            }
            if(jsonObject.containsKey("floatList")) {
                obj.floatList = new ArrayList<Float>();
                for(Object item : (JSONArray)jsonObject.get("floatList")) {
                    obj.floatList.add((Float)item);
                }
            }
            if(jsonObject.containsKey("stringList")) {
                obj.stringList = new ArrayList<String>();
                for(Object item : (JSONArray)jsonObject.get("stringList")) {
                    obj.stringList.add((String)item);
                }
            }
            if(jsonObject.containsKey("objectList")) {
                obj.objectList = new ArrayList<ObjectList>();
                for(Object item : (JSONArray)jsonObject.get("objectList")) {
                    obj.objectList.add(ObjectList.JsonSimpleFactory.fromJsonObject((JSONObject)item));
                }
            }
            return obj;
        }
    }
}
