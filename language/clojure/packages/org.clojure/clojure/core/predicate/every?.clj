; test predicate for every item in a collection

(every? nat-int? [0 1 2])
(every? nat-int? [-1 0 1 2])
(every? nat-int? [0 1 2N]) ; 2N is not fixed precision
