(require
 '[io.pedestal.http :as http]
 '[io.pedestal.http.route :as route]
 '[io.pedestal.interceptor :as interceptor]
 '[io.pedestal.test :as test]
 #_'[org.clojure.edn :as edn]
 '[clojure.test :refer :all])

;; STATE
(def store (atom {}))

;; HANDLERS
(defn list-tasks
  [request]
  (let [task-store (:store request)]
    {:status 200
     :body @task-store}))

(defn save-task
  [request]
  (let [task-store (:store request)
        uuid (java.util.UUID/randomUUID)
        task-name (get-in request [:query-params :name])
        task-status (get-in request [:query-params :status])
        task {:name task-name :status task-status}]
    (swap! task-store assoc uuid task)
    {:status 201
     :body task}))

(defn get-task
  [request]
  (let [task-store (:store request)
        uuid (java.util.UUID/fromString (get-in request [:path-params :id]))
        task (get @task-store uuid)]
    {:status 200
     :body task}))

(defn update-task
  [request]
  (let [task-store (:store request)
        uuid (java.util.UUID/fromString (get-in request [:path-params :id]))
        task (get @task-store uuid)
        updated-name (get-in request [:query-params :name])
        updated-status (get-in request [:query-params :status])
        updated-task (merge task {:name updated-name :status updated-status})]
    (swap! task-store assoc uuid updated-task)
    {:status 201
     :body updated-task}))

(defn delete-task
  [request]
  (let [task-store (:store request)
        uuid (java.util.UUID/fromString (get-in request [:path-params :id]))]
    (swap! task-store dissoc uuid)
    {:status 200
     :body {:message "Removed successfully"}}))

;; INTERCEPTORS
(def db-interceptor
  (interceptor/interceptor
   {:name :db-interceptor ; name of the interceptor
    :enter (fn [context] (update context :request assoc :store store)) ; what to do when it enters the interceptor (must return a new context)
    :leave nil})) ; what to do when it leaves the interceptor

;; ROUTES
#_(def routes #{["/hello" :get `hello-handler :route-name :hello-word]})
(def routes
  (route/expand-routes
   #{["/tasks" :get list-tasks :route-name :list-tasks] ; use [db-interceptor list-tasks] to set an interceptor manually (only the last interceptor receives the request, which is the final handler)
     ["/tasks" :post save-task :route-name :save-task]
     ["/tasks/:id" :get get-task :route-name :get-task]
     ["/tasks/:id" :patch update-task :route-name :update-task]
     ["/tasks/:id" :delete delete-task :route-name :delete-task]}))

;; SERVICE MAP
(def service-map
  (-> {::http/routes routes
       ::http/port 8080
       ::http/type :jetty
       ::http/join? false} ; do not block the thread (good for development)
      (http/default-interceptors) ; add default interceptors (it's automatically with the conventional service-map) 
      (update ::http/interceptors conj db-interceptor) ; add custom interceptors (applies to all routes)
      ))

;; SERVER
(defonce server (atom nil)) ; define the atom only once (even if evaluated multiple times)
(cond (some? @server) (http/stop @server)) ; stop only if there is a server running (good for development hot-restart)
(reset! server (http/start (http/create-server service-map)))

;; TEST
(test/response-for (::http/service-fn @server) :get "/tasks")
(test/response-for (::http/service-fn @server) :post "/tasks?name=football&status=pending")
(test/response-for (::http/service-fn @server) :get "/tasks/90a21a81-304f-4548-8b93-77b04184bf52")
(test/response-for (::http/service-fn @server) :patch "/tasks/86445a37-4c21-4a86-9264-407f7f388ebe?name=football&status=done")
(test/response-for (::http/service-fn @server) :delete "/tasks/9717b7e3-a169-4548-afa7-294c13dc5802")

#_(deftest foo-test
    (testing "test request"
      (let [path "/tasks"
            response (test/response-for (::http/service-fn @server) :get path)
            body (edn/read-string (:body response))]
        (is (some? body)))))
