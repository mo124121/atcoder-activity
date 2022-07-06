#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        A:i32,
        B:i32,
        C:i32,
        X:i32
    }
    let mut ans = 0;
    for i in 0..(A + 1) {
        for j in 0..(B + 1) {
            for k in 0..(C + 1) {
                if X == i * 500 + j * 100 + k * 50 {
                    ans += 1
                }
            }
        }
    }
    println!("{}", ans)
}
