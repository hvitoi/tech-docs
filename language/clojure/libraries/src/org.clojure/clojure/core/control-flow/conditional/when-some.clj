; like "when-let", some it also proceeds with "false" values

(when-some
 [id "aa"]
  id)

(when-some
 [id false]
  id)

(when-some
 [id nil]
  id)
