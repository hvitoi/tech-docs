
; "do" allows executing multiple commands
(if (= 5 5)
  (do (println "Equal - 1st")
      (println "Equal - 2nd"))
  (do (println "Not Equal - 1st")
      (println "Not Equal - 2nd")))