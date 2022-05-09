; match regex pattern

(def book (slurp "https://www.gutenberg.org/files/2701/2701-0.txt"))

(def words (re-seq #"[\w|']+" book))

