; forces walking through the sequence (eager)
(dorun (repeatedly #(println "hi")))
(dorun 5 (repeatedly #(println "hi")))
