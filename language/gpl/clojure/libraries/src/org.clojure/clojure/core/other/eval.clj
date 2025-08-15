;; force the evaluation of a sequence
(-> (seq [:a :b :c :d :e :f])
    doall
    type
    ;
    )
