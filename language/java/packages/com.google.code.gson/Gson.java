import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

class Main {

  public static void main(String[] args) {
    final Gson gson = new GsonBuilder().create();

    // convert
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
