#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use petgraph::unionfind::UnionFind;
use proconio::input;

fn main() {
    input! {
        N:usize,
        sx:i64,
        sy:i64,
        tx:i64,
        ty:i64,
        XYR:[[i64;3];N]
    }
    let mut uf: UnionFind<usize> = UnionFind::new(N + 2);
    for i in 0..N {
        let x1 = XYR[i][0];
        let y1 = XYR[i][1];
        let r1 = XYR[i][2];
        if (sx - x1).pow(2) + (sy - y1).pow(2) == r1.pow(2) {
            uf.union(N, i);
        }
        if (tx - x1).pow(2) + (ty - y1).pow(2) == r1.pow(2) {
            uf.union(N + 1, i);
        }
        for j in 0..N {
            let x2 = XYR[j][0];
            let y2 = XYR[j][1];
            let r2 = XYR[j][2];
            let d = (x1 - x2).pow(2) + (y1 - y2).pow(2);
            if (r1 - r2).pow(2) <= d && d <= (r1 + r2).pow(2) {
                uf.union(i, j);
            }
        }
    }
    if uf.equiv(N, N + 1) {
        println!("Yes")
    } else {
        println!("No")
    }
}
