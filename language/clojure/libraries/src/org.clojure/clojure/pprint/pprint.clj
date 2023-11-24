(require '[clojure.pprint :refer :all])


(def empty-queue clojure.lang.PersistentQueue/EMPTY)

; pretty print
(pprint empty-queue)
(clojure.pprint/pprint empty-queue)
