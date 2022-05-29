;; vec -> map
;; associate key (first arg) for each value (second arg)

(zipmap [:a :b :c :d] [1 2 3 4])
(zipmap [:a :b :c :d] '(1 2 3 4))