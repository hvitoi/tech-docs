
(->> [[3 2 1] [6 5 4]]
     (mapcat reverse))

(->> [[3 2 1] [6 5 4]]
     (map reverse)
     (apply concat)) ;; same!

(->> [[3 2 1] [6 5 4]]
     (map reverse)
     flatten
     concat) ;; same!
