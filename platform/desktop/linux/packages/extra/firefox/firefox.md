# firefox

- <https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data#w_what-information-is-stored-in-my-profile>

## about

- `about:profiles`: all profiles
- `about:config`: all config for a given profile

## Profile

- Stored at `~/.mozilla/firefox/asdf.default/`

- Bookmarks, Downloads, Browsing History
  - **places.sqlite**: bookmarks, downloads, browsing history
  - `bookmarkbackups/`: bookmark backups which can be restored
  - `favicons.sqlite`: favicons for bookmarks
- Passwords
  - `key4.db`: passwords in website
  - `logins.json`: firefox account
- Site-specific preferences
  - `permissions.sqlite`
  - `content-prefs.sqlite`
- Search engines
  - `search.json.mozlz4`: user installed search engines
- Personal dictionary
  - `persdict.dat`: any custom word added to dictionary
- Autocomplete history
  - `formhistory.sqlite`: search bar and forms
- Cookies
  - **cookies.sqlite**: site preferences and login status
- DOM storage
  - `webappsstore.sqlite`: similar to cookies, but more secure
  - `chromeappsstore.sqlite`: information of about pages
- Extensions
  - `extensions`
