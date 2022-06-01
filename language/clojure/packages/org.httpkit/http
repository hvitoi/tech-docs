(require '[org.httpkit.client :as http])

;; fire and forget
;; returns immediately, returned promise is ignored
(http/get "https://reqbin.com/echo/get/json")

(def options {:timeout 200
              :basic-auth ["user" "pass"]
              :query-params {:param "value" :param2 ["value1" "value2"]}
              :user-agent "User-Agent-string"
              :headers {"X-Header" "Value"}})
;; asynchronous response handling
(http/get "https://reqbin.com/echo/get/json" #_options
          (fn [{:keys [status headers body error]}]
            (if error
              (println "Failed, exception is " error)
              (println "Async HTTP GET: " status))))


;; synchronous request
(let [{:keys [status headers body error] :as resp} @(http/request "https://api.plos.org/search?q=title:DNA")]
  (if error
    (println "Failed, exception: " error)
    (println "HTTP GET success: " status)))

;; Form params
(let [options {:form-params {:name "http-kit" :features ["async" "client" "server"]}}
      {:keys [status error]} @(http/post "http://host.com/path1" options)]
  (if error
    (println "Failed, exception is " error)
    (println "Async HTTP POST: " status)))
