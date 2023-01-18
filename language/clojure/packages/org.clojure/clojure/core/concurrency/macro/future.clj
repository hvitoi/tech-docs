; this starts execution in a new thread!
(defn my-async-fn []
  (future
    (println "----------------------------------")
    (println "Done!")
    (println "----------------------------------")
    (recur)))

(my-async-fn)

; "await" for the result (block the current thread)
(println @(my-async-fn)); 


@(do
   (future (Thread/sleep 2000) (println "2nd") "arrived in 2s")
   (future (Thread/sleep 1000) (println "1st") "arrived in 1s"))

(def my-async-fn
  (juxt
   #(future (Thread/sleep 2000) (println "2nd") "arrived in 2s")
   #(future (Thread/sleep 1000) (println "1st") "arrived in 1s")))

(my-async-fn)
