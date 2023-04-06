(empty? []) ; true
(empty? "") ; true
(empty? nil) ; true

(empty? ["a"]) ; false

(read)

(def not-empty? (comp not empty?))
(not-empty? ["a"])

(not-empty ["a"])
(seq ["a"])
