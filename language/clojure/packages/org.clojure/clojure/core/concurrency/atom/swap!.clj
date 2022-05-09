(def my-atom (atom 8))
(def my-atom2 (atom {:a "a", :z 0}))

; update atom with a function (thread safe)
(swap! my-atom inc)
(swap! my-atom2 update :z inc)
(swap! my-atom2 assoc :b "b")
