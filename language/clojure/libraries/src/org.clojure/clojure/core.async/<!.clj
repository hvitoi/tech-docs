(require '[clojure.core.async :as async])

;; prevents blocking the thread
;; but the code won't proceed until a value is received

(def channel (async/chan))

(async/go
  (let [val :foo]
    (async/>! channel val)))

(async/go
  (let [val (async/<! channel)]
    (println val)))
