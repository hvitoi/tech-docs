(def empty-queue clojure.lang.PersistentQueue/EMPTY)

(println empty-queue)
(conj empty-queue 1)
(pop empty-queue) ; pops first