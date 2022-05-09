# Real Time suggestions

- When given a minimum of 2 characters into the search field the system will suggest at most three keywords from the review word repository
- As the customer continues to type in the reviews search bar the relevant keyword suggestions will update automatically
- Output a maximum of 3 keyword suggestions after each character is typed by the customer in the search field.
- If there are more than three acceptable keywords, return the keywords that are first in alphatetical order
- Only return keyword suggestions after the customer has entered 2 characters
  Both the repository and the customerQuery should be compared in case-insensitive way

- Input: repository (array of strings), customerQuery (string representing the full search)
- Output: 2D array of recommendations
