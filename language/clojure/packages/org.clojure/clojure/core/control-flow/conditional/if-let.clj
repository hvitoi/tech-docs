; checks if a parameter exists
(if-let
 [id false]
  (println id)
  (throw (ex-info "id does not exist" {})))
