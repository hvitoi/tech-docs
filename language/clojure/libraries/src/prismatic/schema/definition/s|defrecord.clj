(ns app.defrecord
  (:require [schema.core :as s]))

(s/set-fn-validation! true)

; be careful with s/defrecord, because it can be expanded and therefore "break" the desired schema
(s/defrecord Person
             [id :- Long,
              name :- s/Str])
