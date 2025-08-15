(ns twitter-api.core
  (:require [compojure.core :refer :all]
            [org.httpkit.server :as server]
            [ring.middleware.defaults :refer :all]
            [ring.middleware.json :as mj]
            [twitter-api.handlers :refer :all])
  (:gen-class))

(defroutes app-routes
  (POST "/tweets" [] (mj/wrap-json-body post-twitter-handler {:keywords? true :bigdecimals? true}))
  (GET "/tweets" [] get-twitter-handler))

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (let [port 3000]
    (server/run-server  (wrap-defaults #'app-routes api-defaults)  {:port port})
    (println (str "Running service on port " port))))