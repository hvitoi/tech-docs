class Main {
  public static void main(String[] args) {
    Car myCar = new Car();
    myCar.start();
  }
}

class Engine {
  void start() {
    System.out.println("Engine starting...");
  }
}

class Car {

  private Engine engine;

  public Car() {
    this.engine = new Engine(); // composed inside Car
  }

  public void start() {
    System.out.println("Car is starting...");
    engine.start(); // delegate work to Engine
  }

}
