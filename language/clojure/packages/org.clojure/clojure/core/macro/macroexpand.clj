(defmacro my-macro
  [arg1 arg2 arg3]
  (list arg1 arg2 arg3))


; check the symbol that will be returned by the macro (before evaluating it)
(macroexpand '(my-macro str "hey" "there")) ; => (str "hey" "there")
