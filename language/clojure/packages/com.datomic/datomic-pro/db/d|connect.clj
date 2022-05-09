(require '[datomic.api :as d])

;; connection (the db must exist beforehand)
(def conn (d/connect "datomic:dev://localhost:4334/hello"))

