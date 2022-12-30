(require '[clojure.core.async :refer [chan]])


;; creates a channel without buffer
;; values will be put into the channel only when it's read
(def c (chan))

;; crete a channel with buffer
(def c (chan 5))
