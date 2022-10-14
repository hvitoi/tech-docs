; clojure.lang.ExceptionInfo
(throw (ex-info "some error message" {:type :my-custom-error})) ; the type is used to catch the exact error in the catch block

; additional data in the exception map
(throw (ex-info "some error message" {:additional-data-as-you-want "anything"}))

(throw (Exception.))