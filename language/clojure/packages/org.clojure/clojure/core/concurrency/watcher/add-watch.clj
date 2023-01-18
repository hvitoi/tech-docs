;; react to events
;; e.g., react to atom values being changed

(def token (atom nil))
(add-watch token :my-watcher
           (fn
             [key atom old-state new-state]
             (println "I changed!!" key atom old-state new-state)))

;; change the atom state (the watcher will react)
(reset! token "lala")

(remove-watch token :xWatcher) ; remove a watcher
