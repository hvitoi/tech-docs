(require '[clojure.core.async :refer [chan thread >!!]])

(def c (chan))

;; push the values into a channel
;; first exclamation mark: it has side effect
;; second exclamation mark: it is thread-blocking
(thread
  (doseq [i (range 0 5)]
    (>!! c i)
    (println "Value" i "was put on the channel"))) ; this won't be printed until the value is read
