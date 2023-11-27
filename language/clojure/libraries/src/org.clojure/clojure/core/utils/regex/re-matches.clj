; Returns the match (if any)

(re-matches #"[A-z]" "a") ; => "a"
(re-matches #"[A-z]" "aa") ; => nil (it's not the exact match)
