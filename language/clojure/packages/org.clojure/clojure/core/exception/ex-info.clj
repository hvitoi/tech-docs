(def my-exception
  (ex-info "awesome-message" {:awesome-data "lala"} (ArithmeticException.))) ; the type is used to catch the exact error in the catch block

(type my-exception) ; => clojure.lang.ExceptionInfo 
(ex-message (ex-cause my-exception)) ; => java.lang.ArithmeticException (the nested exception)

(ex-message my-exception) ; => "awesome-message" (same as .getMessage)
(ex-data my-exception) ; => {:awesome-data "lala"}
