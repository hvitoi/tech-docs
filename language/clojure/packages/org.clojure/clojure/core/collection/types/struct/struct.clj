; struct
(defstruct pet :PetType :PetName)

; instance of a struct
(def myDog (struct pet "dog" "Pingo"))

(println (:Name myDog)) ; print a value from the struct