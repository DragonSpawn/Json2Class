package Generated;

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;
import java.util.List;
import java.util.ArrayList;
import org.json.simple.JSONArray;
/***********************************************************************************/
/* This file is generated by Json2Class (https://github.com/DragonSpawn/Json2Class)*/
/* Modifications to this file will be lost the next time you run the tool.         */
/* Date: 2015-03-08                                                                */
/***********************************************************************************/

public class ObjectList{
    public ObjectList() {
        name = "";
    }
    public String name;

    public static class JsonSimpleFactory
    {
        public static String toJson(ObjectList obj) {
            JSONObject json = toJsonObject(obj);
            return json.toString();
        }

        public static String toJson(List<ObjectList> list) {
            JSONArray array = new JSONArray();
            for(ObjectList obj : list)
            {
                array.add(toJsonObject(obj));
            }
            return array.toString();
        }

        public static JSONObject toJsonObject(ObjectList obj) {
            JSONObject json = new JSONObject();
            json.put("name", obj.name);
            return json;
        }
        public static ObjectList fromJson(String jsonString) {
            JSONObject jsonObject = (JSONObject)JSONValue.parse(jsonString);
            return fromJsonObject(jsonObject);
        }

        public static List<ObjectList> fromJsonArray(String jsonArrayString) {
            JSONArray jsonArray = (JSONArray)JSONValue.parse(jsonArrayString);
            List<ObjectList> result = new ArrayList<ObjectList>();
            for(Object jsonObject : jsonArray)
            {
                result.add(fromJsonObject((JSONObject)jsonObject));
            }
            return result;
        }

        public static ObjectList fromJsonObject(JSONObject jsonObject) {
            if(jsonObject == null) {
                return null;
            }
            ObjectList obj = new ObjectList();
            if(jsonObject.containsKey("name")) {
                obj.name = (String)jsonObject.get("name");
            }
            return obj;
        }
    }
}
