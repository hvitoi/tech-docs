fn main() {
    struct Foo;
    struct Bar;
    struct BarFoo;

    impl ops::Sub<Bar> for Foo {
        type Output = BarFoo;
        fn sub(self, _rhs: Foo) -> BarFoo {
            BarFoo
        }
    }

    let a = Foo;
    let b = Bar;
    a - b
}
