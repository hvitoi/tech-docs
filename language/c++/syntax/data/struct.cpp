#include <iostream>
// #include <string>
using namespace std;

// While c structs have only static attributes, c++ structs work similar to
// classes and can have constructors, methods and so on

struct MyVector {
  float x, y;

  // Constructor
  MyVector(float x, float y) : x(x), y(y) { ; }

  // Methods
  MyVector Add(const MyVector &other) const {
    return MyVector(x + other.x, y + other.y);
    // return *this + other; // make the method use the operator instead
    // return operator+(other); // same
  }

  MyVector Multiply(const MyVector &other) const {
    return MyVector(x * other.x, y * other.y);
  }

  // Operator overloading
  MyVector operator+(const MyVector &other) const { return Add(other); }
  MyVector operator*(const MyVector &other) const { return Multiply(other); }
  bool operator==(const MyVector &other) const {
    return x == other.x && y == other.y;
  }
  bool operator!=(const MyVector &other) const {
    return !(*this == other);
    // return !operator==(other); // same
  }
};

// Overload "<<" operator for the "ostream" class
ostream &operator<<(ostream &stream, const MyVector &other) {
  stream << "(" << other.x << ", " << other.y << ")";
  return stream;
};

int main() {
  MyVector position(10.0f, 10.0f);
  MyVector speed(5.0f, 5.0f);
  MyVector powerup(1.1f, 1.1f);

  MyVector result1 = position.Add(speed.Multiply(powerup));
  MyVector result2 = position + speed * powerup; // same!

  cout << result2 << endl;
  return 0;
}
