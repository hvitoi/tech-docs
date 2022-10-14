
; returns the class/var in a namespace if existent, else nil
(ns-resolve 'clojure.core 'assoc)

; current namespace
(ns-resolve *ns* 'assoc)