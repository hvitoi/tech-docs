(def amount 15)

; evaluate expressions and choose only one (the rest is ignored)
(cond
  (= amount 0) (println "zero")
  (< amount 0) (println "negative")
  (> amount 0) (println "positive")
  :else (println "wtf"))

(cond
  (= 1 2) "yeah!") ; returns nil (no matching clause)
