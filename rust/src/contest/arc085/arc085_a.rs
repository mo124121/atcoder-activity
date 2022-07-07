#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N:u32,
        M:u32
    }
    let mut ans: u32 = 1900 * M + 100 * (N - M);
    ans *= 2_u32.pow(M);

    println!("{}", ans)
}

/*期待値は確率の逆数 */
