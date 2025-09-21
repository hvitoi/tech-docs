class Main {
  public static void main(String[] args) {

    try {
      int a = 9 / 0;
    } catch (NullPointerException e) { // won't catch
      e.printStackTrace();
    } catch (IllegalArgumentException e) { // won't catch
      e.printStackTrace();
    } catch (ArrayIndexOutOfBoundsException | ArithmeticException e) { // multi-catch
      e.printStackTrace();
    } catch (Exception e) { // catch all the rest
      e.printStackTrace();
    } finally {
      System.out.println("I will run on success or failure."); // usually to close db connection
    }

  }
}
