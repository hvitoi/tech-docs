void main() {
  /**
   * Static
   */
  UriParse();
  UriHttps();
}

void UriParse() {
  Uri url = Uri.parse('https://example.com/whatsit/create');
}

void UriHttps() {
  Uri url = Uri.https('example.com', 'my/endpoint/create');
}
