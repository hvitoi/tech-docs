(def empty-queue clojure.lang.PersistentQueue/EMPTY)

(conj empty-queue 1)
(pop empty-queue) ; pops first
