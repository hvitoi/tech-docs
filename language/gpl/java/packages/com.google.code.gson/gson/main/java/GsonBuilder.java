import com.google.gson.Gson;
import com.google.gson.GsonBuilder;

class Main {

  public static void main(String[] args) {

    // Static methods
    GsonBuilderNew.run();

    // Instance methods
    GsonBuilderRegisterTypeAdapter.run();
    GsonBuilderCreate.run();
  }
}

class GsonBuilderNew {
  static void run() {
    GsonBuilder builder = new GsonBuilder();

  }
}

class GsonBuilderRegisterTypeAdapter {
  static void run() {
    // defines a custom adapter to serialize into json
    GsonBuilder builder = new GsonBuilder().registerTypeAdapter(String.class, null);
  }
}

class GsonBuilderCreate {
  static void run() {
    Gson gson = new GsonBuilder().create();
  }
}
