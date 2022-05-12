;; this is the actual definition for the comment macro
(defmacro comment
  "Ignores body, yields nil"
  {:added "1.0"}
  [& body])