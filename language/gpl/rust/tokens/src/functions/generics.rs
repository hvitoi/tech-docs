fn main() {
    struct Bar<T>(T);

    fn sum<T: std::ops::Add<Output = T>>(a: T, b: T) -> T {
        a + b
    }

    sum(2_i8, 3_i8);
    sum(2_i32, 3_i32);

    // One type
    struct Point<T> {
        x: T,
        y: T,
    }
    let int_point: Point<i32> = Point { x: 5, y: 10 };
    let float_point: Point<f64> = Point { x: 5.0, y: 10.0 };

    // Multiple types
    struct Foo<T, U> {
        x: T,
        y: U,
    }
    let p: Foo<i32, String> = Foo {
        x: 5,
        y: "hey".to_string(),
    };

    // Impl
    struct Baz<T> {
        bazan: T,
    }
    impl<T> Baz<T> {
        fn get_bazan(&self) -> &T {
            &self.bazan
        }
    }
    let x: Baz<f64> = Baz { bazan: 3.0 };
    let y: Baz<String> = Baz {
        bazan: "hello".to_string(),
    };
    x.get_bazan();
    y.get_bazan();

    // Impl
    struct Buz<T> {
        x: T,
        y: T,
    }
    impl Buz<f64> {
        fn distance_from_origin(&self) -> f64 {
            ((self.x.powi(2)) + self.y.powi(2)).sqrt()
        }
    }
    let p: Buz<f64> = Buz { x: 5.0, y: 10.0 };
    p.distance_from_origin();

    // Const generics
    struct Zaz<T, const N: usize> {
        data: [T; N],
    }
    let foo: [Zaz<i32, 3>; 4] = [
        Zaz { data: [1, 2, 3] },
        Zaz { data: [4, 5, 6] },
        Zaz { data: [7, 8, 9] },
        Zaz { data: [10, 11, 12] },
    ];
}
