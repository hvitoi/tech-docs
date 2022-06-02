;; map is a mixed of eager and lazy
;; it is executed in chunks of 32 elements

;; vector
(map #((+ % 1)) [10 20 30]) ; [11 21 31]
(map inc [10 20 30]) ; [11 21 31]

;; map
(map println {:a 1, :b 2}) ; each element is treated as a vector [key value]

;; sequence
(map println (range 50))

;; linked list
(map println '(0 1 2 3 4 5))


;; Multiple collections (stops when the shortest collection is exhausted)
(map + [1 2 3] '(0 2 4 6 8))
(map (fn [n1 s n2] (str n1 ": " s "-" n2))
     (range)
     ["foo" "bar" "baz"]
     (range 2 -1 -1))


(def data {:grant-type "grant-type"
           :client-id "client-id"
           :client-secret "client-secret"})

(def a #(interpose "=" %&))
(str (a 1 2 3))

(interpose "str")

(->> {:grant-type "grant-type"
      :client-id "client-id"
      :client-secret "client-secret"}
     (map (fn [[key val]] (str key "=" val)))
     (interpose "&")
     (str/join))
