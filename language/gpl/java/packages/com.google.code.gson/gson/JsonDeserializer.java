import java.lang.reflect.Type;

import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;

// optionally you can implement JsonSerializer and JsonDeserializer
class UserAdapter implements JsonDeserializer<User> {

  @Override
  public User deserialize(JsonElement json, Type typeOfT, JsonDeserializationContext context)
      throws JsonParseException {
    JsonObject jsonObject = json.getAsJsonObject();
    JsonElement correlationId = jsonObject.get("correlationid");

    // deserialize everything as User
    User user = context.deserialize(json, typeOfT);

    return user;
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
