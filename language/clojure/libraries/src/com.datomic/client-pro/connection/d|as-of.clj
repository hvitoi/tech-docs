(require '[datomic.client.api :as d])

(def cfg {:server-type :peer-server
          :access-key "myaccesskey"
          :secret "mysecret"
          :endpoint "localhost:8998"
          :validate-hostnames false})
(def client (d/client cfg))
(def conn (d/connect client {:db-name "hello"}))
(def db (d/db conn))

;; ---

;; a snapshot of the database at a point in time
(d/as-of db #inst "2022-03-31")
