#![allow(clippy::let_unit_value)]
use proconio::input;

fn main() {
    input! {
        n:usize,
        mut A:[i32;n],
    };
    let mut ans = 0;
    'outer: loop {
        for a in A.iter_mut().take(n) {
            if *a % 2 == 1 {
                break 'outer;
            } else {
                *a /= 2
            }
        }
        ans += 1
    }
    println!("{}", ans)
}
