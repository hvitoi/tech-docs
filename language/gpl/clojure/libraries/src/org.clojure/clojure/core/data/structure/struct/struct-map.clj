; define struct
(defstruct person :name :age :height)

; instantiate struct
(struct-map person :name "george" :age 22 :height 115)
