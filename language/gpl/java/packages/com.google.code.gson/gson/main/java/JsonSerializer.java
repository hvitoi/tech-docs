import java.lang.reflect.Type;
import java.util.UUID;

import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonSerializationContext;
import com.google.gson.JsonSerializer;

class Main {
  public static void main(String[] args) {
  }
}

// optionally you can implement JsonSerializer and JsonDeserializer
class UserAdapter implements JsonSerializer<User> {

  // defines a custom serialization method
  @Override
  public JsonElement serialize(User src, Type typeOfSrc, JsonSerializationContext context) {
    // empty json
    JsonObject jsonObject = new JsonObject();

    // nest the result of the serialization into a "payload" field in the json
    jsonObject.add("payload", context.serialize(src));

    // add a correlation id into the json
    jsonObject.addProperty("correlationid", src.getName() + UUID.randomUUID().toString());

    return jsonObject;
  }

}

class User {
  String name;
  int age;

  User(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public String getName() {
    return name;
  }

}
