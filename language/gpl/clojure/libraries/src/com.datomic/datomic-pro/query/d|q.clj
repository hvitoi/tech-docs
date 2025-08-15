(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; --- FIND
(-> '[:find ?e ; find spec: relation (collection of lists)
      :where [?e :movie/title]]
    (d/q db)) ; result as [[e1] [e2] [e3]]

(-> '[:find [?e ...] ; find spec: collection (collection)
      :where [?e :movie/title]]
    (d/q db)) ; result as [e1 e2 e3]

(-> '[:find [?e] ; find spec: single tuple (list)
      :where [?e :movie/title]]
    (d/q db)) ; result as [e1] (even if there are more)

(-> '[:find ?e . ; find spec: single scalar (scalar value)
      :where [?e :movie/title]]
    (d/q db))

(-> '[:find ?movie-title
      :where [_ :movie/title ?movie-title "1234" true]] ; filter results from the transaction "1234" only. true: added
    (d/q db))

;; --- WHERE
(-> '[:find ?e
      :where [?e :movie/title]] ; filter entities from datoms that has this attribute associated
    (d/q db))

(-> '[:find (pull ?e [*])
      :where [?e :db/txInstant]] ; filter transaction entities (db/txInstant is the ID 50 with the timestamp of the transaction)
    (d/q db))

(-> '[:find ?title ?year ?genre
      :where
      [?e :movie/title ?title] ; binds a symbol at each where clause
      [?e :movie/release-year ?year]
      [?e :movie/genre ?genre]
      [?e :movie/genre "action/adventure"]
      [(< ?year 2010)] ; predicate
      [(+ 1 ?year) ?year-plus-one] ; custom var
      ]
    (d/q db))

(-> '[:find ?title
      :where [123456 :movie/title ?title]] ; find the specific entity! In this case it's better to use (d/pull db '[*] 123456)
    (d/q db))

(-> '[:find ?movie-name ?genre-name
      :where
      [?movie-id :movie/title ?movie-name]
      [?movie-id :movie/genre ?genre-id]
      [?genre-id :genre/name ?genre-name]] ;; "join" query
    (d/q db))

;; --- IN
(-> '[:find ?e
      :in $ ?my-param ; $ is the db and it's always the first (even when no "in" is used)
      :where [?e :movie/title ?my-param]]
    (d/q db "Spider Man")) ; the parameters to be substituted

; rules
(def rules
  '[;; OR rule (either search by the title or returns the title with spider man)
    [(movie ?e ?title) [?e :movie/title ?title]]
    [(movie ?e ?title) [?e :movie/title ?title] [(ground "Spider Man") ?title]] ; fixes the symbol ?title
    ])
(-> '[:find ?e
      :in $ % ; $: db, %: rules
      :where
      (movie ?e ?title)] ; invokes a rule
    (d/q db rules))

; bindings
(def movie-titles ["Spider Man", "Forrest Gump"])
(-> '[:find ?e
      :in $ [?movie-title ...] ; search for every item in the parameter (one by one)
      :where
      [?e :movie/title ?movie-title]]
    (d/q db movie-titles))

;; --- KEYS
(-> '[:find ?title ?genre
      :keys my-title my-genre ;; return maps instead of tuples
      :where
      [?e :movie/title ?title]
      [?e :movie/genre ?genre]]
    (d/q db))

;; --- WITH
(-> '[:find ?title
      :with ?movie-id ;; consider results with different "movie-id" as different result! (even if the value on the find is the same)
      :where [?movie-id :movie/title ?title]]
    (d/q db))

;; NESTED QUERY
(-> '[:find ?title ?min-release-year
      :where
      [(q '[:find (min ?release-year)
            :where [_ :movie/release-year ?release-year]]
          $) [[?min-release-year]]] ;; binds the result of this subquery into this symbol
      [?e :movie/title ?title]
      [?e :movie/release-year ?min-release-year]]
    (d/q db))
