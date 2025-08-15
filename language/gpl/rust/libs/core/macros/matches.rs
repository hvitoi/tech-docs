fn main() {
    let characters: [char; 5] = ['a', 'E', 'Z', 'x', '9'];

    for el in characters {
        // matches against a list
        assert!(matches!(el, 'A'..='Z' | 'a'..='z' | '0'..='9'));
        // panics if it doesn't match
    }
}
