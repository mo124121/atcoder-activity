#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use petgraph::unionfind::UnionFind;
use proconio::input;

fn main() {
    input! {
        N:usize,
        M:usize,
        P:[usize;N]
    }
    let mut uf: UnionFind<usize> = UnionFind::new(N + 1);
    for i in 0..M {
        input! {
            x:usize,
            y:usize
        }
        uf.union(x, y);
    }
    let mut ans = 0;
    for i in 1..N + 1 {
        if uf.equiv(i, P[i - 1]) {
            ans += 1
        }
    }
    println!("{}", ans);
}
