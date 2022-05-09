(def a (agent 100))

; send a function that will increment the agent asynchronously
(send a inc)

(println @a)
(println "Some time has passed")
(println @a)
