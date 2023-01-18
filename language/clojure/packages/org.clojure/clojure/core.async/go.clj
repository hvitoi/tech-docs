(require '[clojure.core.async :as async])

;; similar to "thread", but a much lighter one (no system threads)

(def channel (async/chan))

(async/go
  (let [val (do
              (println "Building value")
              (Thread/sleep 5000)
              (println "Building finished")
              :foo)]
    (async/>! channel val)))

(async/go
  (let [val (async/<! channel)]
    (println val)))
