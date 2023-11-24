(def o (Object.))


(future (locking o
          (Thread/sleep 5000)
          (println "done1")))

;; Now run this before 5 seconds is up and you'll 
;; find the second instance waits for the first instance to print done1
;; and release the lock, and then it waits for 1 second and prints done2

(Thread/sleep 1000) ; give first instance 1 sec to acquire the lock
(locking o
  (Thread/sleep 1000)
  (println "done2"))
;; => done1
;; => done2
;; => nil

;; locking operates like the synchronized keyword in Java.



; The lock is per value. If 2 different symbols have same value, both are the same lock
(def lock-a "lala")
(def lock-b "lala")

(defn function-that-cannot-be-run-simultaneously
  []
  (println "----------start")
  (Thread/sleep 5000)
  (println "----------end"))

(locking lock-a (function-that-cannot-be-run-simultaneously))

; ---
