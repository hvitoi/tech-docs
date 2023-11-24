(def a (agent 100))

; send a function that will increment the agent asynchronously
(send a inc)

; waits maximum 1s for the amount to be updated (it can be updated before)
(await-for 1000 a)
(println @a)