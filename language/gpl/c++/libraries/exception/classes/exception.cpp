#include <exception>
using namespace std;

// Custom exception
class MyException : public std::exception {
public:
  const char *what() const noexcept override {
    return "Something very bad happened.";
  }
};

int main() {
  throw MyException();
  return 0;
}
