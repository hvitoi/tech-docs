;; ignore the next form
;; often used to temporarily disable some code or some data
#_(println "The reader will not send this function call to the compiler") "This is not ignored"

;; ignore next 2
#_#_(println "The reader will not send this function call to the compiler") "This is not ignored"