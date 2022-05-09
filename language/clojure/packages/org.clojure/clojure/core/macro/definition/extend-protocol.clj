(defprotocol Lifecycle
  (start [component] "started")
  (stop [component] "stopped"))

; extend the protocol
(extend-protocol Lifecycle
  #?(:clj java.lang.Object :cljs default)
  (start [this] this)
  (stop [this] this))