#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]

use proconio::input;

fn binary_search<P>(ok: i64, ng: i64, p: P) -> i64
where
    P: Fn(i64) -> bool,
{
    let mid = (ok + ng) / 2;
    if (ok - ng).abs() == 1 {
        ok
    } else if p(mid) {
        binary_search(mid, ng, p)
    } else {
        binary_search(ok, mid, p)
    }
}

fn main() {
    input! {
        N:usize,
        A:[i64;N]
    }
    let mut max_list = Vec::new();
    for a in A {
        let i = binary_search(max_list.len() as i64, -1, |i| max_list[i as usize] < a) as usize;
        if i < max_list.len() {
            max_list[i] = a
        } else {
            max_list.push(a)
        }
    }

    println!("{}", max_list.len());
}
