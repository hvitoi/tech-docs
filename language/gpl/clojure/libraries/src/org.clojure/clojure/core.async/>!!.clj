(require '[clojure.core.async :as async])

(def channel (async/chan))

;; push the values into a channel
;; first exclamation mark: it has side effect
;; second exclamation mark: it is thread-blocking

(async/go
  (let [val :foo]
    (async/>!! channel val)))

(async/go
  (let [val (async/<!! channel)]
    (println val)))
