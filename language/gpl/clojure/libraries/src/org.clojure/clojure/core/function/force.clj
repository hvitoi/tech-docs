; executes the expression only when it is dereferenced (or forced)
; it can be evaluated only once (the second time it returns the first evaluation)
(def my-uuid
  (delay
    (let [uuid (random-uuid)]
      (print uuid)
      uuid)))

(force my-uuid)

@my-uuid ; same

(force my-uuid)
(force nil)
(force 1)

#(force my-uuid)
(constantly (force my-uuid))
