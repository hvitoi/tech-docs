(map-indexed (fn [i el] (println i el)) ["a" "b" "c"])
(map-indexed (fn [i [k v]] (println i k v)) {:a "a" :b "b"})
