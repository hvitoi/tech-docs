(reduce-kv
 (fn [m k v]
   (println m k v) m)
 {} {:a 1 :b 2})

(reduce-kv
 (fn [m i [k v]]
   (println m i k v))
 {} [[:a "a"] [:b "b"]])
