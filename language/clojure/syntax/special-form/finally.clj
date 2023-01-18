(try
  (/ 1 0)
  (catch ArithmeticException e
    (println "Caught ClassCastException:" (.getMessage e))
    (throw (Exception.)))
  (catch Exception e
    (println "Caught Exception:" (.getMessage e)))
  (catch clojure.lang.ExceptionInfo e
    (println "Caught Exception:" (ex-data e)))
  (finally
    (println "Cleanup and move on")))
