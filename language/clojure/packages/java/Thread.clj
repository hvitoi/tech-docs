; java.lang.Thread

; constructor
(def my-new-thread (Thread. #(println "i will run in a separate thread")))

; start()
(.start my-new-thread)