; define a symbol only once (even if it's evaluate many times)
(defonce server (atom nil))