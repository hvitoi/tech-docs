;; Symbols are defined in a namespace
;; If no ns is set, it's used the namespace "user" by default

; The name of a namespace refers to the directory.file inside the src/ folder
(ns my-app.core
  (:require [clojure.string :refer :all])
  (:use [clojure pprint])
  (:import (java.util Date GregorianCalendar))
  (:gen-class); tells lein to generate a .class for this ns
  )
