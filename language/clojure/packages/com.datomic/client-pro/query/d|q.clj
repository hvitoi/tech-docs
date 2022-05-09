(require '[datomic.client.api :as d])

(def cfg {:server-type :peer-server
          :access-key "myaccesskey"
          :secret "mysecret"
          :endpoint "localhost:8998"
          :validate-hostnames false})
(def client (d/client cfg))
(def conn (d/connect client {:db-name "hello"}))
(def db (d/db conn))

;; --- FIND
(d/q '[:find ?e ; return the ID of the entity
       :where [?e :movie/title]]
     db)

(d/q '[:find ?movie-title ; return an attribute
       :where [_ :movie/title ?movie-title]]
     db)

(d/q '[:find (pull ?e [:movie/title :movie/release-year]) ; extract attributes from the entity
       :where [?e :movie/title]]
     db)

(d/q '[:find (pull ?e [*]) ; extract everything
       :where [?e :movie/title]]
     db)

;; --- WHERE
(d/q '[:find ?e
       :where [?e :movie/title]] ; filter entities from datoms that has this attribute associated
     db)

(d/q '[:find ?title ?year ?genre
       :where
       [?e :movie/title ?title] ; binds a symbol at each where clause
       [?e :movie/release-year ?year]
       [?e :movie/genre ?genre]
       [?e :movie/genre "action/adventure"]
       [(< ?year 2010)]] ; predicate
     db)

(d/q '[:find ?title
       :where [123456 :movie/title ?title]] ; find the specific entity!
     db)

;; --- IN
(d/q '[:find ?e
       :in $ ?my-param ; $ is the db and it's always the first (even when no "in" is used)
       :where [?e :movie/title ?my-param]]
     db
     "The Goonies") ; the parameters to be substituted

;; --- KEYS
(d/q '[:find ?title ?genre
       :keys my-title my-genre ;; return maps instead of tuples
       :where
       [?e :movie/title ?title]
       [?e :movie/genre ?genre]])
