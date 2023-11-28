(def i (atom 0)) «

(while (< @i 10)
  (println @i)
  (swap! i inc)
  "not-returned")
