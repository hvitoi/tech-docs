# HTML Scraping

## API (Application Programming Interface)

The service explicitly exposes endpoints (usually HTTP/REST or GraphQL) that return structured data, typically JSON or XML.
You call a documented URL like GET <https://api.example.com/users/123> and get back {"id": 123, "name": "..."}.
Pros: stable contract, structured data, authenticated, rate-limited but sanctioned, fast.
Cons: only exposes what the provider chose to expose; may require keys, quotas, or payment.

## HTML scraping

You fetch the same HTML page a browser would render and parse the markup (with tools like `BeautifulSoup`, `Cheerio`, `Playwright`) to extract data from the DOM.
Example: download <https://example.com/users/123>, then find `<h1 class="username">` and read its text.
Pros: works on any site, no API needed, can extract anything visible.
Cons: fragile (breaks when HTML changes), slower, may violate ToS, often blocked (CAPTCHAs, bot detection), needs a headless browser if the page is JS-rendered.
