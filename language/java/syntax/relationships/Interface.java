// Interface is an Abstract Class with all methods abstract
// It's like a contract. And who signs it must implements the abstract methods defined
// Interfaces do not contain attributes
interface Authenticable {
  void setPassword(int password);

  boolean authenticate(int password);
}

class Employee {
  private double salary;

  protected double getSalary() {
    return salary;
  }

  protected void setSalary(double salary) {
    this.salary = salary;
  }

}

// A class can implement multiple interfaces
class Boss extends Employee implements Authenticable {

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

  public double getBonus() {
    return super.getSalary();
  }

}
