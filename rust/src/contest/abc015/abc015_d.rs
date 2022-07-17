#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]

use proconio::input;

fn main() {
    input! {
        W:usize,
        N:usize,
        K:usize,
        AB:[[usize;2];N]
    }
    let mut dp = vec![vec![vec![0_usize; W + 1]; K + 1]; N + 1];

    for i in 0..N {
        let a = AB[i][0];
        let b = AB[i][1];
        for k in 0..K + 1 {
            for w in 0..W + 1 {
                dp[i + 1][k][w] = std::cmp::max(dp[i + 1][k][w], dp[i][k][w]);
                if w + a <= W && k < K {
                    dp[i + 1][k + 1][w + a] =
                        std::cmp::max(dp[i + 1][k + 1][w + a], dp[i][k][w] + b)
                }
            }
        }
    }

    let mut ans = 0;
    for k in 0..K + 1 {
        for w in 0..W + 1 {
            ans = std::cmp::max(ans, dp[N][k][w])
        }
    }

    println!("{}", ans);
}

/*
解けはしたけど想定解じゃない
添え字が消せるみたいだし、最短のコードを確認すべき
*/
