(defn fn1 []
  (Thread/sleep 2000)
  (println "fn1")
  "a")
(defn fn2 []
  (Thread/sleep 2000)
  (println "fn2")
  "b")

; prints "fn1" after 2 s
; prints "fn2" after 4 s
; returns ["a" "b"] after 4 s
(apply (juxt fn1 fn2) [])
