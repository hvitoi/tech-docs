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

(try
  (inc "abc")
  (catch clojure.lang.ExceptionInfo e
    (cond
      (= :my-error-1 (:type (ex-data e))) "My Error One"
      (= :my-error-2 (:type (ex-data e))) "My Error Two"
      :else (throw e) ; rethrow in case it's not the exception you want (bad pattern)
      )))