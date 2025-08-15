import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

import org.apache.kafka.common.serialization.Serializer;

// Serializers can be used as KEY/VALUE_SERIALIZER_CLASS_CONFIG

class Main {
  public static void main(String[] args) {
  }
}

class JsonSerializer<T> implements Serializer<T> {
  private final Gson gson = new GsonBuilder().create();

  @Override
  public byte[] serialize(String topic, T data) {
    return gson.toJson(data).getBytes();
  }

}

class User {
  String name;
  int age;
}
