(require '[schema.core :as s])

(s/defschema MySchema (s/enum :a :b :c))
(s/defschema MySchema (apply s/enum #{:a :b :c})) ; same

(s/validate MySchema :a)
