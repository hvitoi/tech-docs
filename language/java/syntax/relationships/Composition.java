class Main {
  public static void main(String[] args) {

    Client client = new Client();
    client.setPassword(123);
    System.out.println(client.authenticate(123));

  }
}

class AuthenticationUtil {
  private int password;

  public void setPassword(int password) {
    this.password = password;
  }

  public int getPassword() {
    return this.password;
  }

  public boolean authenticate(int password) {
    if (this.password == password) {
      return true;
    }
    return false;
  }

}

class Client {

  private AuthenticationUtil authenticator;

  public Client() {
    this.authenticator = new AuthenticationUtil(); // compose with a new object
  }

  // delegate the method to the util instance
  public void setPassword(int password) {
    this.authenticator.setPassword(password);
  }

  // delegate the method to the util instance
  public boolean authenticate(int password) {
    return this.authenticator.authenticate(password);
  }

}
