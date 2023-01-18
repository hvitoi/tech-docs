(import (java.util.concurrent ThreadFactory))

;; receives a "Java class"/"Record" or a "Java interface"/"Protocol"
;; returns an Object implementing this class/interface

(def ^:private default-thread-factory
  (let [!count (atom 0)]
    (reify ThreadFactory
      (newThread [_ r]
        (doto (Thread. r)
          (.setName (format "chime-%d" (swap! !count inc))))))))
