(def a (agent 100))

(send a inc)

; when agent returns error (e.g., 2 threads updating the agent at the same time)
(println (agent-error a))
