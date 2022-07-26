
(reduce-kv (fn [m k v] (println m k v) m) {} {:a 1 :b 2})
