;; cat concatenates nested collections

(into [] cat [[1 2] [3 4]])

(sequence cat [[1 2] [3 4]])

(transduce cat conj [] [[1 2] [3 4]])
