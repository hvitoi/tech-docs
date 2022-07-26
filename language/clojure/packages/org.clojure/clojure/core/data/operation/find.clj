;Returns the map entry for key, or nil if key not present.

(find {:a 1 :b 2 :c 3} :a)
;;=> [:a 1]

(find {:a nil} :a)
;;=> [:a nil]

(find {:a 1 :b 2 :c 3} :d)


(find [:a :b :c :d] 2)
;;=> [2 :c]

(find [:a :b :c :d] 5)
;;=> nil

(find [1 2 3] 4294967296)
;;=> [4294967296 1]
