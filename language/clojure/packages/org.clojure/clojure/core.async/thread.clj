(require '[clojure.core.async :refer [chan thread >!! <!!]])

(def c (chan))

;; "thread" is similar to "future", but instead of returning a promise, returns a channel

; push values into channel
(thread
  (doseq [i (range 0 5)]
    (>!! c i)
    (println "Value" i "was put on the channel")))

; pull values out of channel
(thread
  (doseq [_ (range 0 5)]
    (->> (<!! c)
         (println "got:"))))
