(require '[clojure.core.async :as async])

; channels allow "putting" values on one thread and "taking" values on another thread

;; creates a channel without buffer
;; values will be put into the channel only when it's read
(def channel (async/chan))

;; create a channel with buffer
;; values will be put into the channel right away (respecting the max buffer)
;; if the buffer is full, than additional values will be put only after the last one is taken
(def channel (async/chan 5))

(type channel) ; => clojure.core.async.impl.channels.ManyToManyChannel
