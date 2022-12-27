val myRegex = """.* ([\d]+).*""".r // regex for numbers only (.r means it's a regular expression)
val myRegex(myFilteredNumbers) = "To life, the universe, and everything is 42." // apply regex to a string
