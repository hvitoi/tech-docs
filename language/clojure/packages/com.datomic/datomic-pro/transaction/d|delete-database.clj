(require '[datomic.api :as d])

;; delete database
(d/delete-database "datomic:dev://localhost:4334/hello")
