fn main() {
    #[derive(PartialEq, Debug)]
    struct Foo;

    let a = Foo;
    let b = Foo;

    assert_eq!(a, b);
}
