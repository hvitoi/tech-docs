; Return all the pattern matches in a string
; Returned as a lazy sequence

(def book-str
  (slurp "https://www.gutenberg.org/files/2701/2701-0.txt"))

; get all the whole words from a string
(re-seq #"[\w|']+" book-str)

; get all the individual letters in a string
(re-seq #"[A-z]" "Heyy!")

; returns truthy if the last character is not a letter or digit
(re-seq #"[^A-z]$" "hey!")
