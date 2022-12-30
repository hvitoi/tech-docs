(require '[clojure.core.async :refer [chan thread put! take!]])

(def c (chan))

(thread
  (put! c "my value!!"
        (fn [sent?]
          (println "this is my callback function (this is print in repl). Has been sent?:" sent?))))

(thread
  (take! c
         (fn [value]
           (println "this is my callback function. Value taken:" value))))
