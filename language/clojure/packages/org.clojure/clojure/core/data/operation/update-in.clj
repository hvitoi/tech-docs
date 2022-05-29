;; map
(def data {:k1 1, :k2 2, :k3 {:a 3, :b 4}})
(update-in data [:k3 :a] inc) ; update nested element
