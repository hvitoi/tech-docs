import scala.io.Codec

// set a encoding for a document different than UTF-8
implicit val codec: Codec = Codec("ISO-8859-1")
