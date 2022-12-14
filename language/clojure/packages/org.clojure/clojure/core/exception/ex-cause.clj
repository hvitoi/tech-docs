; return the nested exception (ArithmeticException)
(ex-cause (ex-info "awesome-message" {:awesome-data "lala"} (ArithmeticException.)))
