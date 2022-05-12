import java.util.Map;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.apache.kafka.common.serialization.Deserializer;

// Deserializers can be used as KEY/VALUE_DESERIALIZER_CLASS_CONFIG

class Main {
  public static void main(String[] args) {

  }
}

class JsonDeserializer<T> implements Deserializer<T> {
  private final Gson gson = new GsonBuilder().create();
  private Class<T> classToDeserializeTo;

  @Override
  public void configure(Map<String, ?> configs, boolean isKey) {
    // get any property that has been set on "configs.setProperty()"
    String className = (String) configs.get("my.config.type-to-deserialized");

    // get the class from a string
    this.classToDeserializeTo = Class.forName(typeName);

    // Deserializer.super.configure(configs, isKey);
  }

  @Override
  public T deserialize(String topic, byte[] data) {
    return gson.fromJson(new String(data), classToDeserializeTo);
  }

}

class User {
  String name;
  int age;
}
