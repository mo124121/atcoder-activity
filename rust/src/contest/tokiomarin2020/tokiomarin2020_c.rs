#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N:usize,
        K:i32,
        mut A:[usize;N]
    }
    for i in 0..std::cmp::min(K, 41) {
        let mut imos = vec![0i32; N];
        for j in 0..N {
            if j < A[j] {
                imos[0] += 1;
            } else {
                imos[j - A[j]] += 1;
            }

            let r = j + A[j] + 1;
            if r < N {
                imos[r] -= 1;
            }
        }
        A[0] = imos[0] as usize;
        for j in 0..N - 1 {
            A[j + 1] = (A[j] as i32 + imos[j + 1]) as usize;
        }
    }
    println!(
        "{}",
        A.iter()
            .map(|i| i.to_string())
            .collect::<Vec<String>>()
            .join(" ")
    )
}
