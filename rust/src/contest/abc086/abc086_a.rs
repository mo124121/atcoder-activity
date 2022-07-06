#![allow(clippy::let_unit_value)]
use proconio::input;

fn main() {
    input! {
        //from OnceSource::from(""),
        a:i32,
        b:i32,
    }
    if a * b % 2 == 0 {
        println!("Even");
    } else {
        println!("Odd")
    }
}
