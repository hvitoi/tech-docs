(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; --- FIND
(d/q '[:find ?e ; find spec: relation (collection of lists)
       :where [?e :movie/title]]
     db) ; result as [[e1] [e2] [e3]]

(d/q '[:find [?e ...] ; find spec: collection (collection)
       :where [?e :movie/title]]
     db) ; result as [e1 e2 e3]

(d/q '[:find [?e] ; find spec: single tuple (list)
       :where [?e :movie/title]]
     db) ; result as [e1] (even if there are more)

(d/q '[:find ?e . ; find spec: single scalar (scalar value)
       :where [?e :movie/title]]
     db)


(d/q '[:find ?movie-title
       :where [_ :movie/title ?movie-title "1234" true]] ; filter results from the transaction "1234" only. true: added
     db)

;; --- WHERE
(d/q '[:find ?e
       :where [?e :movie/title]] ; filter entities from datoms that has this attribute associated
     db)

(d/q '[:find (pull ?e [*])
       :where [?e :db/txInstant]] ; filter transaction entities (db/txInstant is the ID 50 with the timestamp of the transaction)
     db)

(d/q '[:find ?title ?year ?genre
       :where
       [?e :movie/title ?title] ; binds a symbol at each where clause
       [?e :movie/release-year ?year]
       [?e :movie/genre ?genre]
       [?e :movie/genre "action/adventure"]
       [(< ?year 2010)] ; predicate
       [(+ 1 ?year) ?year-plus-one] ; custom var
       ]

     db)

(d/q '[:find ?title
       :where [123456 :movie/title ?title]] ; find the specific entity! In this case it's better to use (d/pull db '[*] 123456)
     db)

(d/q '[:find ?movie-name ?genre-name
       :where
       [?movie-id :movie/title ?movie-name]
       [?movie-id :movie/genre ?genre-id]
       [?genre-id :genre/name ?genre-name]] ;; "join" query
     db)

;; --- IN
(d/q '[:find ?e
       :in $ ?my-param ; $ is the db and it's always the first (even when no "in" is used)
       :where [?e :movie/title ?my-param]]
     db
     "Spider Man") ; the parameters to be substituted

; rules
(def rules
  '[;; OR rule (either search by the title or returns the title with spider man)
    [(movie ?e ?title) [?e :movie/title ?title]]
    [(movie ?e ?title) [?e :movie/title ?title] [(ground "Spider Man") ?title]] ; fixes the symbol ?title
    ])
(d/q '[:find ?e
       :in $ % ; $: db, %: rules
       :where
       (movie ?e ?title)] ; invokes a rule
     db
     rules)

; bindings
(def movie-titles ["Spider Man", "Forrest Gump"])
(d/q '[:find ?e
       :in $ [?movie-title ...] ; search for every item in the parameter (one by one)
       :where
       [?e :movie/title ?movie-title]]
     db
     movie-titles)

;; --- KEYS
(d/q '[:find ?title ?genre
       :keys my-title my-genre ;; return maps instead of tuples
       :where
       [?e :movie/title ?title]
       [?e :movie/genre ?genre]]
     db)

;; --- WITH
(d/q '[:find ?title
       :with ?movie-id ;; consider results with different "movie-id" as different result! (even if the value on the find is the same)
       :where [?movie-id :movie/title ?title]]
     db)

;; NESTED QUERY
(d/q '[:find ?title ?min-release-year
       :where
       [(q '[:find (min ?release-year)
             :where [_ :movie/release-year ?release-year]]
           $) [[?min-release-year]]] ;; binds the result of this subquery into this symbol
       [?e :movie/title ?title]
       [?e :movie/release-year ?min-release-year]]
     db)
