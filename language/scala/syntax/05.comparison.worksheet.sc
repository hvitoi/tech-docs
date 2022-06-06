val isGreater = 1 > 2
val isLesser = 1 < 2
val impossible = isGreater & isLesser // bitwise and
val logicalAnd = isGreater && isLesser // logical and
val logicalOr = isGreater || isLesser // logical or

val picard: String = "Picard"
val bestCaptain: String = "Picard"
val isBest: Boolean = picard == bestCaptain
