
(defn my-async-fn
  []
  (future
    (Thread/sleep 1000)
    "result available after 1s"))

; "await" for the result (block the current thread)
(println @(my-async-fn)); 
