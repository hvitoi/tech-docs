(require '[clojure.core.async :as async])

; close a channel manually
(def channel (async/chan))

(async/close! channel)
