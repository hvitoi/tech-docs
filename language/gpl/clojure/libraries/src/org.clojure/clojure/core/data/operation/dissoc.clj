;; remove element

;; map
(def data {:k1 "v1", :k2 "v2"})
(dissoc data :k1) ; remove element
(dissoc data :k1 :k2) ; remove elements
(dissoc data :k9) ; remove non-existent element
