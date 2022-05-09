(defrecord Person [id name age])


(record? (->Person 1 "henry" 27)); true