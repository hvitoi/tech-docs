(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

; all data, including the ones removed (false)
(def complete-db (d/history db))

(-> '[:find ?e ?status ; shows "true" and "false" statuses (normal db would show only true)
      :where [?e :movie/title ?title ?tx ?status]]
    (d/q complete-db))
