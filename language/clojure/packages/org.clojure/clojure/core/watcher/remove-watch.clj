;; react to events
;; e.g., react to atom values being changed

(def a (atom 5))
(add-watch a
           :xWatcher (fn [key atom old-state new-state]
                       (println key atom old-state new-state)))

;; change the atom state (the watcher will react)
(reset! a 10)

(remove-watch a :xWatcher) ; remove a watcher
