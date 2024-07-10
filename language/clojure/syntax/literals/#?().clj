;; Reader conditional https://clojure.org/guides/weird_characters#_reader_conditional

;; add different behaviors for clojure and clojurescript code

(defn parse-int [s]
  #?(:clj (Long/parseLong s)
     :cljs (js/parseInt s)))

#?(:clj  (Clojure expression)
   :cljs (ClojureScript expression)
   :cljr (Clojure CLR expression)
   :default (fallthrough expression))
