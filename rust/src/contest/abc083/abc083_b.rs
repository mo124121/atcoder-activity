#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N:u32,
        A:u32,
        B:u32
    }
    let mut ans = 0;
    for i in 1..(N + 1) {
        let s = i
            .to_string()
            .chars()
            .map(|c| c.to_digit(10).unwrap())
            .sum::<u32>();

        if A <= s && s <= B {
            ans += i
        }
    }
    println!("{}", ans)
}
