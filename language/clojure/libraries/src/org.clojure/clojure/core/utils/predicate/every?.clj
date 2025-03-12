; test predicate for every item in a collection

(every? even? [0 2 4 6])
(every? even? [0 2 4 5 6])

; --

(def words #{:foo :bar})
(every? words [:foo :bar]) ; true
(every? words [:foo :bar :baz]) ; false
