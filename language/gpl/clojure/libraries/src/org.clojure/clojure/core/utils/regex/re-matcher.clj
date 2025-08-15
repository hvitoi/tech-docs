; Creates a matcher (regex + string) to be used

(def *matcher* (re-matcher #"\d+" "abc12345def"))
(re-find *matcher*)
