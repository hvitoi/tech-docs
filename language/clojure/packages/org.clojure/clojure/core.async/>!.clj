(require '[clojure.core.async :as async])

;; prevents blocking the thread

(def channel (async/chan))

(async/go
  (let [val :foo]
    (async/>! channel val)))

(async/go
  (let [val (async/<! channel)]
    (println val)))
