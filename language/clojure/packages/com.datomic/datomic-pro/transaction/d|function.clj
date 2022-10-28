(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; custom transactions are run in the transactor (server) in a serialized way

;; custom transaction
(def increment-views
  (d/function '{:lang :clojure
                :params [e value]
                :code [[:db/add e :movie/views value]]}))

;; custom transaction (different syntax)
(def increment-views
  #db/fn {:lang :clojure
          :params [db movie-id]
          :code (let [views (d/q '[:find ?views .
                                   :in $ ?movie-id
                                   :where
                                   [?e :movie/id ?movie-id]
                                   [?e :movie/views ?views]]
                                 db
                                 movie-id)
                      new-views (if (number? views) (inc views) 1)]
                  [{:movie/id movie-id :movie/views new-views}])})

;; install function (it's actually a new attribute)
(d/transact conn [{:db/ident :increment-views
                   :db/fn increase-views
                   :db/doc "this function increases the number of views (:movie/views)"}])

;; invoke function
(d/transact conn [[:increment-views "1234"]])
