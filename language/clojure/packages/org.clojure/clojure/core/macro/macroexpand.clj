; check the actual content of a macro

(macroexpand '(when 'this-is-true
                'evaluate-this))