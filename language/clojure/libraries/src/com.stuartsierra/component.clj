(require '[com.stuartsierra.component :as component])

;; Define Components
(defrecord Database []
  component/Lifecycle

  ;; what to do when the component starts for the first time
  (start [this]
    (assoc this :store (atom {}))) ; create a new database

  ;; what to do when the components stops
  (stop [this]
    (assoc this :store nil))) ; remove the database

(defrecord Printer [database]
  component/Lifecycle

  (start [this]
    (let [store (:store database)]
      (println @store)
      "I am a printer, but i do not print"))

  (stop [this] ()))


(defn new-database [] (->Database))
(defn new-printer [] (map->Printer {})) ; component lib will inject here the necessary dependencies


;; Add Components to the component-system
(defn component-system []
  (component/system-map
   :database (new-database)
   :printer (component/using (new-printer) [:database]) ; :printer depends on :database
   ))


;; Start the system-map
(def component-result
  (component/start (component-system)))

(:database component-result)
(:printer component-result)
