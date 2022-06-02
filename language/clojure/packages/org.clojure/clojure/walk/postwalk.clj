(require '[clojure.walk :as walk])


(def counter (atom -1))
(def line-counter (atom 0))
(def print-touch
  (fn [x]
    (print (swap! line-counter inc) ":" (pr-str x) "→ ")))
(def change (fn [x]
              (let [new-x (swap! counter inc)]
                (prn new-x)
                [new-x x])))

(walk/postwalk (fn [x]
                 (print-touch x)
                 (change x))
               {:a 1 :b 2})