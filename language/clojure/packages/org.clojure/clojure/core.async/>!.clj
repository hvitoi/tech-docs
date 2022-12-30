(require '[clojure.core.async :refer [chan go >! <!]])

;; prevents blocking the thread

(let [c (chan)]
  (go
    (doseq [i (range 0 5)]
      (>! c i)
      (println "Value" i "was put on the channel")))

  (go
    (doseq [_ (range 0 5)]
      (->> (<! c)
           (println "got:")))))
