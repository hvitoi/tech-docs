; executes the expression only when it is dereferenced (or forced)
; it can be evaluated only once (the second time it returns the first evaluation)
(def my-uuid
  (delay
   (random-uuid)))

(force my-uuid)

@my-uuid ; same
