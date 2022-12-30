(require '[clojure.core.async :refer [chan go >! <!]])

;; tasks created inside of a "go routine" is much lighter than a thread

(let [c (chan)]
  (go
    (doseq [i (range 0 5)]
      (>! c i)
      (println "Value" i "was put on the channel")))

  (go
    (doseq [_ (range 0 5)]
      (->> (<! c)
           (println "got:")))))
