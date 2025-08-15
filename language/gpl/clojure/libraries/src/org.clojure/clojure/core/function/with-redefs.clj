(with-redefs [repeatedly (fn [_] "a")]
  (repeatedly '_))


;; ---
(ns lol
  (:require user))

(user/greeting)
(with-redefs [user/person "Josh!"]
  (user/greeting))
