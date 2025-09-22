import java.math.BigInteger;

// similar to the primitive integer types but allows arbitrary large values
// E.g., 50! = 30414093201713378043612608166064768844377641568960512000000000000
// It is widely used in security and cryptography applications

class Main {
  public static void main(String[] args) {
    _new();

    // Static Methods
    _valueOf();
  }

  static void _new() {
    var biFromString = new BigInteger("1234567890987654321");
    var biFromByteArray = new BigInteger(new byte[] { 64, 64, 64, 64, 64, 64 });
    var biFromSignMagnitude = new BigInteger(-1, new byte[] { 64, 64, 64, 64, 64, 64 });
  }

  static void _valueOf() {
    var bi = BigInteger.valueOf(2305843009213693951L);
  }
}
