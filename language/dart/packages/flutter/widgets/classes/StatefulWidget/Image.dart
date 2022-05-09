import 'package:flutter/widgets.dart';

Widget main() {
  return Image(
    image: NetworkImage(
        'https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg'),
  );
}

Widget mainAsset() {
  return Image.asset(
    'assets/images/waiting.png', // must be added in pubspec.yaml
    fit: BoxFit.cover,
  );
}

Widget mainNetwork() {
  return Image.network(
      'https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Gull_portrait_ca_usa.jpg/1920px-Gull_portrait_ca_usa.jpg');
}
