(ns app.set-fn-validation!
  (:require [schema.core :as s]))

; activate schema validation for function parameters
(s/set-fn-validation! true) ; false by default
