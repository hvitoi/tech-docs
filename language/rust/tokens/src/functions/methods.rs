/*
  Methods are Associated functions
  Associated functions can or cannot depend on self
*/

struct Rectangle {
    width: u32,
    height: u32,
}

// The methods can also be split across multiple `impl` blocks
impl Rectangle {
    // Associated function (doesn't depend on self)
    fn new(width: u32, height: u32) -> Self {
        // Self refers to Rectangle
        Self { width, height }
    }

    // Associated function (depends on self - method)
    // fn area(self: &Self ) -> u32 { // same
    fn area(&self) -> u32 {
        // self or &self don't matter here since it's ints are copied
        self.width * self.height
    }
}

fn main() {
    let my_rect: Rectangle = Rectangle::new(5, 10);
    let rect_area: u32 = my_rect.area();
    println!("{}", rect_area);
}
