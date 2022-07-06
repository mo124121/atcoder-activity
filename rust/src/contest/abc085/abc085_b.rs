#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use std::collections::HashSet;

use proconio::input;

fn main() {
    input! {
        N:usize,
        D:[u32;N]
    }
    let mut uniq = HashSet::new();
    for d in D {
        uniq.insert(d);
    }
    println!("{}", uniq.len());
}
