#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {N:i64}
    let MOD = 998244353;
    let ans = (1..)
        .take_while(|a| a * a <= N)
        .map(|a| ((N / a) - a + 2) / 2)
        .sum::<i64>()
        % MOD;

    println!("{}", ans);
}
