(defproject app "0.1.0"
  ;; :repositories {"my.datomic.com" {:url "https://my.datomic.com/repo"
  ;;                                  :username [:env/my_datomic_username] ; export MY_DATOMIC_USERNAME= "your@email.com"
  ;;                                  :password [:env/my_datomic_password] ; export MY_DATOMIC_PASSWORD= "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
  ;;                                  #_#_:creds :gpg}} ; ~/.lein/credentials.clj.gpg (optional)
  :dependencies [[org.clojure/clojure "1.11.0"]
                 [org.clojure/test.check "1.1.1"]
                 [prismatic/schema "1.1.12"]
                 [prismatic/schema-generators "0.1.4"]
                ;;  [com.datomic/datomic-pro "1.0.6362"] ; peer mode (pro version)
                 [com.datomic/datomic-free "0.9.5697"] ; peer mode (free version)
                 [com.datomic/client-pro "1.0.74"] ; client mode (pro version)
                 ])
