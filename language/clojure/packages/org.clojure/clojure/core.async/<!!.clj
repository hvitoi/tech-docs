(require '[clojure.core.async :as async])

(def channel (async/chan))

(async/go
  (let [val :foo]
    (async/>!! channel val)))

(async/go
  (let [val (async/<!! channel)]
    (println val)))
