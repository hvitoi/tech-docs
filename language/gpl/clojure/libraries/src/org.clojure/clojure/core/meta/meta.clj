(defn i-have-attributes
  {:doc "Docs can be added like this too"
   :foo "Any attributes you fancy"}
  []
  "Good for you")

;; return metadata of an object
(meta #'i-have-attributes)

; ---

(defn foo
  [a b]
  1)

(meta #'foo)
