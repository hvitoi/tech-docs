(require '[clojure.set :refer [join]])

(def a
  [{:id 1 :name "henry"}
   {:id 2 :name "john"}
   {:id 3 :name "lauren"}])

(def b
  [{:id 1 :age 28}
   {:id 2 :age 29}
   {:id 4 :age 5}])

(join a b {:id :id})
