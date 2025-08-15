(require '[datomic.client.api :as d])

(def cfg {:server-type :peer-server
          :access-key "myaccesskey"
          :secret "mysecret"
          :endpoint "localhost:8998"
          :validate-hostnames false})
(def client (d/client cfg))
(def conn (d/connect client {:db-name "hello"}))

; ---

; transact (attributes/schema)
(->> {:tx-data
      [{:db/ident :movie/title
        :db/valueType :db.type/string
        :db/cardinality :db.cardinality/one
        :db/doc "The title of the movie"}

       {:db/ident :movie/genre
        :db/valueType :db.type/string
        :db/cardinality :db.cardinality/one
        :db/doc "The genre of the movie"}

       {:db/ident :movie/release-year
        :db/valueType :db.type/long
        :db/cardinality :db.cardinality/one
        :db/doc "The year the movie was released in theaters"}

       {:db/ident :movie/comments
        :db/valueType :db.type/string
        :db/cardinality :db.cardinality/many
        :db/doc "Comments about the movie"}]}
     (d/transact conn))

; transact (data)
(->> {:tx-data
      [{:movie/title "The Goonies"
        :movie/genre "action/adventure"
        :movie/release-year 1985
        :movie/comments ["Comment 1" "Comment 2"]}

       {:movie/title "Commando"
        :movie/genre "action/adventure"
        :movie/release-year 1985}

       {:movie/title "Repo Man"
        :movie/genre "punk dystopia"
        :movie/release-year 1984}]}
     (d/transact conn))

;; :db/add
(->> {:tx-data
      [[:db/add "17592186045472" :movie/release-year 2009] ; remove + add
       [:db/add "17592186045472" :movie/comments "Comment 3"] ; add
       [:db/add "17592186045472" :movie/comments "Comment 4"] ; add
       ]}
     (d/transact conn))

;; :db/retract (remove only)
(->> {:tx-data
      [[:db/retract "17592186045472" :movie/release-year 2009] ; remove
       [:db/retract "17592186045472" :movie/comments "Comment 3"]]}
     (d/transact conn))
