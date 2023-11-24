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
(-> '[:find ?e ; return the ID of the entity
      :where [?e :movie/title]]
    (d/q db))

(-> '[:find ?movie-title ; return an attribute
      :where [_ :movie/title ?movie-title]]
    (d/q db))

(-> '[:find (pull ?e [:movie/title :movie/release-year]) ; extract attributes from the entity
      :where [?e :movie/title]]
    (d/q db))

(-> '[:find (pull ?e [*]) ; extract everything
      :where [?e :movie/title]]
    (d/q db))

;; --- WHERE
(-> '[:find ?e
      :where [?e :movie/title]] ; filter entities from datoms that has this attribute associated
    (d/q db))

(-> '[:find ?title ?year ?genre
      :where
      [?e :movie/title ?title] ; binds a symbol at each where clause
      [?e :movie/release-year ?year]
      [?e :movie/genre ?genre]
      [?e :movie/genre "action/adventure"]
      [(< ?year 2010)]] ; predicate
    (d/q db))

(-> '[:find ?title
      :where [123456 :movie/title ?title]] ; find the specific entity!
    (d/q db))

;; --- IN
(-> '[:find ?e
      :in $ ?my-param ; $ is the db and it's always the first (even when no "in" is used)
      :where [?e :movie/title ?my-param]]
    (d/q db "The Goonies")) ; the parameters to be substituted

;; --- KEYS
(-> '[:find ?title ?genre
      :keys my-title my-genre ;; return maps instead of tuples
      :where
      [?e :movie/title ?title]
      [?e :movie/genre ?genre]]
    (d/q db))
