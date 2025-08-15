(def my-exception
  (ex-info "awesome-message"
           {:awesome-data "lala"}
           (ArithmeticException.))) ; the type is used to catch the exact error in the catch block

my-exception
(ex-message my-exception)
(ex-data my-exception)
(ex-cause my-exception)
(.printStackTrace my-exception)
(prn-str my-exception)

(type my-exception) ; => clojure.lang.ExceptionInfo
(ex-message (ex-cause my-exception)) ; => java.lang.ArithmeticException (the nested exception)

(ex-message my-exception) ; => "awesome-message" (same as .getMessage)
(ex-data my-exception) ; => {:awesome-data "lala"}
