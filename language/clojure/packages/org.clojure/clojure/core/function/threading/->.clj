;; THREAD FIRST
;; threads to the first argument of the next function

(def my-map {:k1 {:a 1 :b 2}
             :k2 {:c 3 :d 4}})

(-> my-map :k1 :a)

;; -> is usually used for collections
;; ->> is usually used fpr sequences
