; ensure that a reference has not been changed

(def colors
  {:blue (ref 0)
   :green (ref 0)
   :red (ref 0)
   :honeypots (ref 0)})

(defn batch [prefs]
  (future
    (dosync
     (ensure (:honeypots colors))
     (doseq [color prefs
             :while (< @(:honeypots colors) 3)]
       (update colors color commute inc)))))

(let [b1 (batch [:red :honeypots :green :blue :blue :red :honeypots])
      b2 (batch [:green :blue :blue :green :red :blue :red :red])
      b3 (batch [:honeypots :blue :red :red :blue :green :green :red])]
  [@b1 @b2 @b3]
  {:total-votes (reduce + (map deref (vals colors)))
   :winner (ffirst (sort-by (comp deref second) > colors))
   :fraud? (= @(:honeypots colors) 3)})

;; {:total-votes 16, :winner :blue, :fraud? true}