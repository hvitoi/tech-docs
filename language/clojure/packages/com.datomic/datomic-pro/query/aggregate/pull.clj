(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

(-> '[:find (pull ?e [:movie/title :movie/release-year]) ; extract attributes from the entity
      :where [?e :movie/title]]
    (d/q db))

(-> '[:find (pull ?e [*]) ; extract everything
      :where [?e :movie/title]]
    (d/q db))

;; FORWARD NAVIGATION (populate nested entities) 
(-> '[:find (pull ?movie-id [:movie/title {:movie/genre [:genre/id :genre/name]}])
      :where
      [?genre-id :genre/name "action"]
      [?movie-id :movie/genre ?genre-id]]
    (d/q db))

(-> '[:find (pull ?movie-id [* {:movie/genre [*]}]) ; all + :movie/genre populated
      :where
      [?genre-id :genre/name "action"]
      [?movie-id :movie/genre ?genre-id]]
    (d/q db))

;; BACKWARD NAVIGATION (finds who references a certain entity)
(-> '[:find (pull ?genre-id [:genre/name {:movie/_genre [:movie/title :movie/release-year]}])
      :where
      [?genre-id :genre/name]]
    (d/q db))
