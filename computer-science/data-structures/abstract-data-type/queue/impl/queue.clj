(defprotocol IQueue
  (add-el [this element])
  (remove-el [this])
  (peek-el [this]))

(defrecord Queue [q]
  IQueue
  (add-el [_ el]
    (swap! q conj el))
  (remove-el [_]
    (swap! q next))
  (peek-el [_]
    (first @q)))
