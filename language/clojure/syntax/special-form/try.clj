(try
  (inc "abc")
  (catch ClassCastException e
    (println "Caught ClassCastException:" (.getMessage e)))
  (catch Exception e
    (println "Caught Exception:" (.getMessage e)))
  (catch clojure.lang.ExceptionInfo e
    (println "Caught Exception:" (ex-data e)))
  (finally
    (println "Cleanup and move on")))
