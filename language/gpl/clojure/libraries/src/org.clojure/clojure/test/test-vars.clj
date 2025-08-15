(require '[clojure.test :as test])

; like test-var, but receives a list of functions
(test/test-vars [#'namespace1/function-test
                 #'namespace2/function-test])
