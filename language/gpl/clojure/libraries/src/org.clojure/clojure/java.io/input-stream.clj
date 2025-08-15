(require '(clojure.java [io :as io]))

;; Create a input stream from a file or URI
(defn file->bytes [file]
  (with-open [xin (io/input-stream file)
              xout (java.io.ByteArrayOutputStream.)]
    (io/copy xin xout)
    (.toByteArray xout)))

;; create input stream from a string
(-> "lalala"
    (.getBytes "UTF-8")
    ByteArrayInputStream.)
