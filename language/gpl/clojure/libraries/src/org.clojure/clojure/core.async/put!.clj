(require '[clojure.core.async :as async])

;; same as >! but accepts callback

(def channel (async/chan 5))

(async/thread
  (let [val :foo
        callback (fn [sent?]
                   (println "A value has been put?" sent?))]
    (async/put! channel val callback)))

(async/thread
  (let [callback (fn [value]
                   (println "Got value" value))]
    (async/take! channel callback)))
