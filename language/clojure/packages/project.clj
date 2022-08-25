(defproject app "0.1.0-SNAPSHOT"
  ;; :repositories {"my.datomic.com" {:url "https://my.datomic.com/repo"
  ;;                                  :username [:env/my_datomic_username] ; export MY_DATOMIC_USERNAME= "your@email.com"
  ;;                                  :password [:env/my_datomic_password] ; export MY_DATOMIC_PASSWORD= "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  ;;                                  #_#_:creds :gpg}} ; ~/.lein/credentials.clj.gpg (optional)
  :description "Sample snippets"
  :url "http://example.com/sample"
  :license {:name "Eclipse Public License"
            :url "https://www.eclipse.org/legal/epl-2.0/"}
  :dependencies [[org.clojure/clojure "1.11.0"]
                 [org.clojure/data.json "2.4.0"]
                 [org.clojure/test.check "1.1.1"]
                 [prismatic/schema "1.1.12"]
                 [prismatic/schema-generators "0.1.4"]
                ;;  [com.datomic/datomic-pro "1.0.6362"] ; peer mode (pro version)
                 [com.datomic/datomic-free "0.9.5697"] ; peer mode (free version)
                 [com.datomic/client-pro "1.0.74"] ; client mode (pro version)
                 [io.pedestal/pedestal.service "0.5.10"] ; web framework
                ;;  [io.pedestal/route "0.5.10"] ; web framework
                 [io.pedestal/pedestal.jetty "0.5.10"] ; web server backend
                 [com.stuartsierra/component "1.1.0"]
                 [http-kit "2.3.0"]]
  :repl-options {:init-ns user})
