import 'dart:io';

void main() {
  Platform.environment; // all environment variables
  Platform.operatingSystem; // e.g., linux (not recommended for verification)

  // true/false
  Platform.isAndroid;
  Platform.isFuchsia;
  Platform.isIOS;
  Platform.isLinux;
  Platform.isMacOS;
  Platform.isWindows;
}
