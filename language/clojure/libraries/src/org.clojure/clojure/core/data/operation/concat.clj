;; concatenate

;; vec
(concat [1 2 3] [4 5 6])
(concat [1 2 3] #{4 5 6})

(concat {:a "a"} {:b "b"})

;; seq
(concat (seq [1 2 3]) (seq [4 5 6]))
