(parse-uuid "e0ff4f5c-246d-4910-894a-344afc6eec32")
(parse-uuid nil)

(defn parse-uuid-safe
  [s]
  (try
    (parse-uuid s)
    (catch Throwable _ s)))
