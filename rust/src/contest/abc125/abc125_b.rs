#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {N:i64}
    let mut ans = 0;
    let MOD = 998244353;
    let mut q = 1;
    while q * q <= N {
        ans += ((N / q) - q + 2) / 2;
        ans %= MOD;
        q += 1;
    }

    println!("{}", ans);
}
