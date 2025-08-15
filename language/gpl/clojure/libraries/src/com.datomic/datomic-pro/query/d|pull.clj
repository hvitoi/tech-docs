(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; pull by entity
(d/pull db '[*] 17592186045418)

;; pull by any unique attribute (returns one entity only)
;; LOOKUP REFS
(d/pull db '[*] [:movie/id 1234])
