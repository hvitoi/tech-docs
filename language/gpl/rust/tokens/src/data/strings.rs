fn main() {
    // String (String)
    // Allocated in heap, owns the data and it's mutable
    // Stored as a vector of bytes (Vec)
    let s: String = String::from("hello word"); // pointer to heap

    // String Slices (&str)
    // Allocated in stack, does not own the data and it's immutable
    // str itself can never be used as a type, only as a reference

    let foo: &str = &s; // &String is converted to &str implicitly
    let hello: &str = &s[0..5];
    let word: &str = &s[6..11];
    let hey: &str = "hey Ru\x73t!"; // \x73 is the hexadecimal representation of 's'
    let unicode_codepoint: &str = "\u{211D}"; // U+211D
    let long_string: &str = "String literals
                                can span multiple lines.";
    let raw_string: &str = r"Escapes don't work here";
    let quotes: &str = r#"And then I said: "There is no escape!""#;
    let quotes: &str = r##"And then I said: "I need a # in the quote!""##;
    let h: &str = &quotes[0..2]; // slice of the array of bytes. Range from the start in bytes

    // String Literal ("")
    // Allocated in read-only memory, hardcoded into the executable, immutable
    // Fixed size, it's value is valid throughout the entire lifetime of the program
    let hardcoded: &str = "hello world"; // it's also a string slice

    // Boxed string
    let a: Box<str> = "hello world".into();
}
