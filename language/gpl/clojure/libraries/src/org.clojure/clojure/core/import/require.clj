;; options
(require 'my-other-ns)
(require 'clojure.string :reload) ; force reloading the ns (even if it has been loaded before)
(require 'clojure.string :reload-all) ; force reloading all the imported namespaces
(require 'clojure.repl :verbose)

;; vectors
(require '[clojure.string :refer :all]) ; import all symbols
(require '[clojure.string :refer [capitalize]]) ; import a single symbol
(require '[clojure.string :as str]) ; with alias


;; import multiple
(require 'clojure.repl 'clojure.test '[clojure.string :as str])
(require '(clojure string test)) ; import clojure.string & clojure.test
(require '(clojure [string :as string] test))

; invoke symbols from namespaces
(my-other-ns/hello)
