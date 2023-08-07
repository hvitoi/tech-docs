fn main() {
    struct Foo;
    struct Bar;
    struct FooBar;

    impl ops::Add<Bar> for Foo {
        type Output = FooBar;
        fn add(self, _rhs: Bar) -> FooBar {
            FooBar
        }
    }

    let a = Foo;
    let b = Bar;
    a + b
}
