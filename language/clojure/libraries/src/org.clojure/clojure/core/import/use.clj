;; you can use "(require xxx :refer :all)" 
(use 'clojure.string)
(use '[clojure.string]) ; import all the symbols
(use '[clojure.string :only [capitalize]]) ; pick specific symbols
(use '[clojure.string :exclude [replace reverse]]) ; pick all symbols except ...
(use '[clojure.string :rename {replace str-replace, reverse str-reverse}]) ; pick specific symbols and rename
(use '[clojure.string :as str]) ; import all with a symbol
