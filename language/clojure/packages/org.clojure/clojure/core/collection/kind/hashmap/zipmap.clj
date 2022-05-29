; transforms a vector into a hashmap, associate a key for each vector element

(->> [1 2 3 4]
     (zipmap [:a :b :c :d]))

(zipmap [:a :b :c :d] '(1 2 3 4))