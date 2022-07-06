#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
            N:usize,
        mut A:[i32;N]
    }
    A.sort_by(|a, b| b.cmp(a));
    let mut scores = [0; 2];
    for i in 0..N {
        scores[i % 2] += A[i];
    }
    println!("{}", scores[0] - scores[1])
}
