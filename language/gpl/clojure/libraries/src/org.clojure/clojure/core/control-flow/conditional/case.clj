(def pet "fish")

; the constant must be a compile time literal! No symbols or forms

(case pet
  "cat"          "It's a cat"
  ("dog" "fish") "It's a dog or a fish"
  (str "default value to be returned" :a))

;; if no clause is met and there is no default clause, a error its thrown
