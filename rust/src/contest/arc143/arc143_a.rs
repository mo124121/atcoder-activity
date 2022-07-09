#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        mut A:[u64;3]
    }
    A.sort();
    A.reverse();

    if A[0] - A[1] <= A[2] {
        let mut ans = 0_u64;
        ans += A[0] - A[1];
        A[0] -= ans;
        A[2] -= ans;
        ans += A[0];
        println!("{}", ans)
    } else {
        println!("-1")
    }
}
