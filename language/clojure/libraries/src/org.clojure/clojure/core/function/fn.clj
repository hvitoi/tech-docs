; annomynous function
; one-line function

(fn [x] (+ x 9))
#(+ %1 9) ; same function, %1 is the first arg

(defn wrap-with-logging [func]
  (fn [& args]
    (let [result (apply func args)]
      (println "Log result: " result)
      result)))

((fn [x & _] x) 9 8 7)
