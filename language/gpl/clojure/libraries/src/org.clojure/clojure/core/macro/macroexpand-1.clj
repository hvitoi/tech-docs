; macros are functions that transform lists into other lists

; "when" is transformed into a "if". Because "when" is a macro
(macroexpand-1 '(when true (println "hello")))
