(require '[clojure.core.async :as async])

; creates a channel that will automatically close after x seconds

(def channel (async/timeout 5000))

; when the channel is closed, it no longer receives new values
(async/go
  (let [val :foo]
    (async/>! channel val)))

; when the channel is closed, returns nil right away
; but values entered before the channel closed are received even after it's closed
(async/go
  (let [val (async/<! channel)]
    (println val)))
