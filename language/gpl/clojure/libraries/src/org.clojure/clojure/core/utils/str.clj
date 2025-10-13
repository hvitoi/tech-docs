; concatenate to form a string
; string is a vector of characters

(str "a" "b")

(str 23 (apply + [2 3]) (:foo {:foo "foo"}))

(str ["b" "c"])

(str [\a \b \c])

(subs (str :foo/bar) 1)
