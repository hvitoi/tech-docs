#include <stdexcept>
using namespace std;

int main() {
  // Used in scenarios of empty container
  throw underflow_error("Something wrong happened.");
  return 0;
}
