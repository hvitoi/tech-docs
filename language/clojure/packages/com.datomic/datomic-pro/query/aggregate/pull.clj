(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

(d/q '[:find (pull ?e [:movie/title :movie/release-year]) ; extract attributes from the entity
       :where [?e :movie/title]]
     db)

(d/q '[:find (pull ?e [*]) ; extract everything
       :where [?e :movie/title]]
     db)

;; FORWARD NAVIGATION (populate nested entities) 
(d/q '[:find (pull ?movie-id [:movie/title {:movie/genre [:genre/id :genre/name]}])
       :where
       [?genre-id :genre/name "action"]
       [?movie-id :movie/genre ?genre-id]]
     db)

(d/q '[:find (pull ?movie-id [* {:movie/genre [*]}]) ; all + :movie/genre populated
       :where
       [?genre-id :genre/name "action"]
       [?movie-id :movie/genre ?genre-id]]
     db)

;; BACKWARD NAVIGATION (finds who references a certain entity)
(d/q '[:find (pull ?genre-id [:genre/name {:movie/_genre [:movie/title :movie/release-year]}])
       :where
       [?genre-id :genre/name]]
     db)
