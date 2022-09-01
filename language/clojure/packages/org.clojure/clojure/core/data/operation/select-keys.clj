
; pick some key-values from a map
(select-keys {:a 1 :b 2 :c 3} #{:a :b})
(select-keys {:a 1 :b 2 :c 3} [:a])
