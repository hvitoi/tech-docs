(if (= 5 5)
  (println "Equal")
  (println "Not equal"))

(if (and (= 5 5) (or (= 2 2) (not true)))
  (println "Truthy")
  (println "Falsy"))

(if (= 5 5)
  (do (println "Equal - 1st")
      (println "Equal - 2nd"))
  (do (println "Not Equal - 1st")
      (println "Not Equal - 2nd")))
