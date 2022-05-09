(defrecord Person [id name age])

;; Invoke constructor
(map->Person {:id 1, :name "Henry", :age 27}) ; same