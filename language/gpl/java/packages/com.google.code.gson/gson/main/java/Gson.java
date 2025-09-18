import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

class Gson {

  public static void main(String[] args) {
    /**
     * Static
     */
    GsonNew.run();

    /**
     * Instance
     */
    GsonToJson.run();
  }
}

class GsonNew {
  static Gson run() {
    Gson gson = new GsonBuilder().create();
    return gson;
  }
}

class GsonToJson {
  static void run() {
    Gson gson = GsonNew.run();

    User obj = new User("henry", 99);
    String json = gson.toJson(obj);

  }
}

class User {
  String name;
  int age;

  User(String name, int age) {
    this.name = name;
    this.age = age;
  }

}
