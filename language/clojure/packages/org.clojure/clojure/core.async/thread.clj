(require '[clojure.core.async :as async])

(def channel (async/chan))

;; "thread" is similar to "future", but instead of returning a promise, returns a channel

; push values into channel
(async/thread
  (let [val (do
              (println "Building value")
              (Thread/sleep 5000)
              (println "Building finished")
              :foo)]
    (async/>! channel val)))

; pull values out of channel
(async/thread
  (let [val (async/<! channel)]
    (println val)))
