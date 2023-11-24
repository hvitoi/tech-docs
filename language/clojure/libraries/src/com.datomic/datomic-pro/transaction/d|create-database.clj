(require '[datomic.api :as d])

;; protocol dev
(d/create-database "datomic:dev://localhost:4334/hello")

;; protocol mem
(d/create-database "datomic:mem://hello")
