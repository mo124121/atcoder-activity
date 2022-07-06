#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N:u32,
        Y:u32
    }
    for i in 0..N + 1 {
        for j in 0..N + 1 - i {
            let s = i * 10000 + j * 5000;
            if s <= Y && (Y - s) / 1000 == N - i - j {
                println!("{} {} {}", i, j, N - i - j);
                return;
            }
        }
    }
    println!("-1 -1 -1")
}
