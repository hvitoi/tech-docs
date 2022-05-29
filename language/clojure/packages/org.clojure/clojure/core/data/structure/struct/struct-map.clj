; struct
(defstruct pet :PetType :PetName)

; instance of a struct
(def myDog (struct-map pet :PetType "dog" :PetName "Pingo"))
