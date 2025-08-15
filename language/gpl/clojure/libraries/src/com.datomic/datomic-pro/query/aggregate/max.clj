(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

(-> '[:find (max ?release-year)
      :where
      [_ :movie/release-year ?release-year]]
    (d/q db))
