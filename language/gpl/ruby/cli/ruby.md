# ruby CLI

- `-r` is the CLI flag for require a package

```shell
ruby -rsecurerandom -e 'puts SecureRandom.alphanumeric(22)'
```

Same as:

```ruby
require "securerandom"

puts SecureRandom.alphanumeric(22)
```

```shell
ruby myfile.rb
```
