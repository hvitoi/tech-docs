; let define symbols escoped to this form (let form) only!

;; vector destructuring
(def my-vector [1 2 3 4 5])
(let [[a b c] my-vector] (print a b c)) ; 1 2 3
(let [[a b _ c] my-vector] (print a b c)) ; 1 2 4
(let [[a b & rest] my-vector] (print a b rest)) ; 1 2 (3 4 5)
(let [[a b :as all] my-vector] (print a b all)) ; 1 2 (1 2 3 4 5)

;; hashmap destructuring
(def my-map {:alpha "A", :beta "B", "gamma" "G", 'delta "D"})
(let [{a :alpha b :beta o :omega} my-map] (print a b o)) ; A B nil
(let [{:keys [alpha beta omega] :or {omega "default-value"}
       :strs [gamma]
       :syms [delta]
       :as all} my-map]
  (print alpha beta gamma delta omega all)) ; A B G D {:alpha "A", :beta "B", "gamma" "G", 'delta "D"}

;; vector of maps destructuring
(def my-map-vector [{:alpha "A"} {:beta1 "B1" :beta2 "B2"}])
(let [[_ {b2 :beta2}] my-map-vector]
  (print b2))

;; multiple assignments
(let [full-price 99
      discount-rate (/ 10 100)
      discount (* full-price discount-rate)]
  (- full-price discount))

;; variable shadowing
(def foo "a")
(let [foo "b"] (println foo)) ; b
(println foo) ; a
