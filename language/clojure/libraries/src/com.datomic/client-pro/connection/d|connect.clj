(require '[datomic.client.api :as d])

;; configuration
(def cfg {:server-type :peer-server
          :access-key "myaccesskey"
          :secret "mysecret"
          :endpoint "localhost:8998"
          :validate-hostnames false})

;; client
(def client (d/client cfg))

;; connection
(def conn (d/connect client {:db-name "hello"}))

