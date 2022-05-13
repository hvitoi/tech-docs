; throw ExceptionInfo
(throw (ex-info "some error message" {}))

; throw java exception
(throw (java.lang.IllegalStateException. "Description"))
