(require '[clojure.set :refer [join]])

(def set-a
  {:id 1 :name "henry"}
  {:id 2 :name "john"})

(def set-b
  {:id 1 :age 28}
  {:id 2 :name 29})

(join set-a set-b {:id :id})
