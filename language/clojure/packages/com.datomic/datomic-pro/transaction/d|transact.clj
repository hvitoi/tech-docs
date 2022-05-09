(require '[datomic.api :as d])
(require '[schema.core :as s])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))

; --- plumatic schemas
(def Genre
  {:genre/id java.util.UUID
   :genre/name s/Str})
(def Movie
  {:movie/id java.util.UUID
   :movie/title s/Str
   :movie/release-year s/Num
   (s/optional-key :movie/genre) Genre
   :movie/comments [s/Str]})


; transact (attributes/schema)
(d/transact conn [{:db/ident :tx-data/ip ; additional transaction info
                   :db/valueType :db.type/string
                   :db/cardinality :db.cardinality/one}])

(d/transact conn [{:db/ident :genre/id ;; defines an ID for each genre
                   :db/valueType :db.type/uuid
                   :db/cardinality :db.cardinality/one
                   :db/unique :db.unique/identity}
                  {:db/ident :genre/name ;; defines an ID for each genre
                   :db/valueType :db.type/string
                   :db/cardinality :db.cardinality/one}])

(d/transact conn [{:db/ident :movie/title
                   :db/valueType :db.type/string
                   :db/cardinality :db.cardinality/one
                   :db/doc "The title of the movie"}

                  {:db/ident :movie/genre
                   :db/valueType :db.type/ref ;; reference to the genre attribute created before
                   :db/cardinality :db.cardinality/one
                   :db/doc "The genre of the movie"}

                  {:db/ident :movie/release-year
                   :db/valueType :db.type/long
                   :db/cardinality :db.cardinality/one
                   :db/doc "The year the movie was released in theaters"}

                  {:db/ident :movie/views
                   :db/valueType :db.type/long
                   :db/cardinality :db.cardinality/one
                   :db/noHistory true ; do not record old values about this attribute
                   }

                  {:db/ident :movie/comments
                   :db/valueType :db.type/string
                   :db/cardinality :db.cardinality/many
                   :db/isComponent true ; if it's a component, when the entity is fetched it brings its nested data (no forward navigation necessary). Components are removed in cascade
                   :db/doc "Comments about the movie"}

                  {:db/ident :movie/id
                   :db/valueType :db.type/uuid ; if you want to create the entity ID by yourself
                   :db/cardinality :db.cardinality/one
                   :db/unique :db.unique/identity ; tells that this ID will be unique (any insert with same ID will replace values)
                   }])

; transact (data)
(def action-genre-uuid (java.util.UUID/randomUUID))
(def starwars-movie-uuid (java.util.UUID/randomUUID))
(d/transact conn [[:db/add "datomic.tx" :tx-data/ip "192.168.0.1"] ; add the ip to the transaction entity
                  {:genre/name "action"
                   :genre/id action-genre-uuid}])

(d/transact conn [[:db/add "datomic.tx" :tx-data/ip "192.168.0.1"] ; add the ip to the transaction entity
                  {:movie/title "Star Wars"
                   :movie/genre [:genre/id action-genre-uuid] ; reference to another entity
                   :movie/release-year 1977
                   :movie/comments ["Comment 1" "Comment 2"]
                   :movie/id starwars-movie-uuid ; random uuid for the entity
                   }

                  {:movie/title "Spider Man"
                   :movie/genre [:genre/id action-genre-uuid] ;; lookup
                   :movie/release-year 2002}

                  {:movie/title "Forrest Gump"
                   :movie/genre {:genre/name "drama"
                                 :genre/id (java.util.UUID/randomUUID)} ; create an entity on the fly
                   :movie/release-year 1994}])

; temporary ID
(d/transact conn [{:db/id "lol-temp" ; temporary id (just to reference it for the insert below)
                   :genre/name "comedy"}
                  {:movie/title "Click"
                   :movie/genre "lol-temp" ; reference to the category created above
                   :movie/release-year 2006}])


;; :db/add (upsert)
(d/transact conn [[:db/add "17592186045472" :movie/release-year 2009] ; remove + add
                  [:db/add "17592186045472" :movie/comments "Comment 3"] ; add
                  [:db/add "17592186045472" :movie/comments "Comment 4"] ; add
                  [:db/add [:movie/id starwars-movie-uuid] :movie/genre [:genre/id action-genre-uuid]] ; lookup ref (because movie/genre is a reference)
                  ])

;; :db/retract (remove)
(d/transact conn [[:db/retract "17592186045472" :movie/release-year 2009] ; remove
                  [:db/retract "17592186045472" :movie/comments "Comment 3"]])

;; :db/retractEntity (remove)
(d/transact conn [[:db/retractEntity [:movie/id starwars-movie-uuid]] ; remove the whole entity (all attributes)
                  ])

;; :db/cas (compare and set)
(d/transact conn [[:db/cas [:movie/id starwars-movie-uuid] :movie/release-year 1977 2040]]) ; if it has value 1977 change to 2040 (or else throw IllegalStateExceptionInfo)
