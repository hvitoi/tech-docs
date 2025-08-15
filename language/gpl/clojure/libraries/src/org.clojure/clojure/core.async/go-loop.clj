(require '[clojure.core.async :as async])

(def channel (async/chan))

;; same as (go (loop ...))
(async/go-loop
 [i 0]
  (when (< i 5)
    (async/>! channel i)
    (recur (inc i))))

(async/go
  (let [val (async/<! channel)]
    (println "got" val)))

(async/go-loop
 []
  (println "I am printing forever" (rand-int 10))
  (async/<! (async/timeout 5000)) ; similar to a "sleep" (it will return nil only after the channel is closed, until there it will hang)
  (recur))

(def print-forever
  (delay
    (let [a (atom nil)]
      (async/go-loop [_ true]
        (reset! a (rand-int 10))
        (println "Forever printing" @a)
        (recur (async/<! (async/timeout 5000)))))))

(realized? print-forever)
@print-forever
(realized? print-forever)
