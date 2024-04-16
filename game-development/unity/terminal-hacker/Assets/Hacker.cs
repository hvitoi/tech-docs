using UnityEngine;

public class Hacker : MonoBehaviour
{
  // Game configuration data
  enum Screen { MainMenu, Password, Win } // Enumeration type
  string[] levelOnePasswords = { "books", "aisle", "shelf", "password", "font", "borrow" };
  string[] levelTwoPasswords = { "prisoner", "handcuffs", "holster", "uniform", "arrest" };
  string[] levelThreePasswords = { "starfield", "telescope", "environment", "exploration", "astronauts" };

  // Member variables - hold the state
  int level;
  Screen currentScreen;
  string password;


  void Start() // Start is a "message"
  {
    ShowMainMenu();
  }

  void ShowMainMenu()
  {
    currentScreen = Screen.MainMenu;
    Terminal.ClearScreen();
    Terminal.WriteLine("What would you like to hack into?");  // This is a statement
    Terminal.WriteLine("Press 1 for the local library");
    Terminal.WriteLine("Press 2 for the police station");
    Terminal.WriteLine("Press 3 for NASA");
    Terminal.WriteLine("Enter your selection:");
  }

    void OnUserInput(string input)
    {
      if (input == "menu") ShowMainMenu();  // C# doesn't accept comparison between different data types
      else if (input == "quit" || input == "close")
      {
        Application.Quit();
      }

    switch (currentScreen)
    {
      case Screen.MainMenu:
        CheckLevel(input);
        break;
      case Screen.Password:
        CheckPassword(input);
        break;
      default:
        ShowMainMenu();
        break;
    }

  }

  void CheckLevel(string input)
  {
    bool isValidLevel = (input == "1" || input == "2" || input == "3");

    if (isValidLevel)
    {
      level = int.Parse(input);
      StartLevel();
    }
    else if (input == "007") Terminal.WriteLine("Please select a level Mr Bond!");
    else Terminal.WriteLine("Please choose a valid level.");
  }



  void StartLevel()
  {
    currentScreen = Screen.Password;
    Terminal.ClearScreen();
    SetRandomPassword();
    Terminal.WriteLine("Enter your password, hint: " + password.Anagram());
    Terminal.WriteLine("You can write 'menu' at any time.");
  }

  void SetRandomPassword()
  {
    switch (level)
    {
      case 1:
        password = levelOnePasswords[Random.Range(0, levelOnePasswords.Length)];
        break;
      case 2:
        password = levelTwoPasswords[Random.Range(0, levelTwoPasswords.Length)];
        break;
      case 3:
        password = levelThreePasswords[Random.Range(0, levelThreePasswords.Length)];
        break;
      default:
        Debug.LogError("Invalid level number"); // Log error to the console
        break;
    }
  }

  void CheckPassword(string input)
  {
    if (input == password) DisplayWinScreen();
    else StartLevel();
  }


  void DisplayWinScreen()
  {
    currentScreen = Screen.Win;
    Terminal.ClearScreen();
    ShowLevelReward();
  }

  void ShowLevelReward()
  {
    switch (level)
    {
      case 1:
        Terminal.WriteLine("Congratulations! Have a book.");  // Multiline string
        Terminal.WriteLine(@"     
    _______
   /      //
  /      //
 /_____ //
(______(/  
        ");
        break;

      case 2:
        Terminal.WriteLine("Congratulations! Have a prison key.");
        Terminal.WriteLine(@"     
 __
/0 \_______
\__/-=' = '  
        ");
        break;

      case 3:
        Terminal.WriteLine("Welcome to NASA's internal system!");
        Terminal.WriteLine(@"  
 _ __   __ _ ___  __ _
| '_ \ / _` / __|/ _` |
| | | | (_| \__ \ (_| |
|_| |_|\__,_|___)\__,_|
        ");
        break;

      default:
        Debug.LogError("Invalid level");
        break;
    }
  }

}