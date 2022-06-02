; checks if a parameter exists
(if-let
 [id false]
  (println id)
  (throw (ex-info "id does not exist" {})))


(def foo {})
(if-let [{:keys [a b]} foo]
  true
  false)
