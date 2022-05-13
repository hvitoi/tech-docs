(defrecord Person [id name age])

;; Invoke constructor
(->Person 1 "Henry" 27) ; same
(map->Person {:id 1, :name "Henry", :age 27}) ; same