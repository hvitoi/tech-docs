class Main {
  public static void main(String[] args) {
  }
}

// Interface is an Abstract Class with all methods abstract
// It's like a contract. And who signs it must implements the methods
// Interfaces do not contain fields
interface Authenticable {
  void setPassword(int password);

  boolean authenticate(int password);
}

class Person {
  private String name;

  protected String getName() {
    return name;
  }

  protected void setName(String name) {
    this.name = name;
  }
}

// A class can implement multiple interfaces
class Employee extends Person implements Authenticable {
  private int password;

  @Override
  public void setPassword(int password) {
    this.password = password;
  }

  @Override
  public boolean authenticate(int password) {
    if (this.password == password) {
      return true;
    }
    return false;
  }
}
