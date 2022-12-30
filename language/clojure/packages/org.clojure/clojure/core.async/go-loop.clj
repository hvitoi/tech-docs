(require '[clojure.core.async :refer :all])

;; tasks created inside of a "go routine" is much lighter than a thread

(let [c (chan)]
  (go-loop
   (doseq [i (range 0 5)]
     (>! c i)
     (println "Value" i "was put on the channel")))

  (go
    (doseq [_ (range 0 5)]
      (->> (<! c)
           (println "got:")))))


(type (go-loop [_ true]
        (println "I am printing forever" (rand-int 10))
        (recur (<! (timeout 5000)))))

(def print-forever
  (delay
    (let [a (atom nil)]
      (go-loop [_ true]
        (reset! a (rand-int 10))
        (println "Forever printing" @a)
        (recur (<! (timeout 5000)))))))

(realized? print-forever)
@print-forever
(realized? print-forever)
