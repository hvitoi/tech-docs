(def pet "dog")

; the constant must be a compile time literal! No symbols or forms

(case pet
  "cat" (println "It's a cat")
  "dog" (println "It's a dog")
  "fish" (println "It's a fish")
  (str "default value to be returned" :a))

;; if no clause is met and there is no default clause, a error its thrown

(case (-> {:a 1} :a)
  (-> {:a 1} :a) "lol")