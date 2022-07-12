#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        N:usize,
        K:usize,
        A:[i32;N],
        B:[usize;K]
    }
    let mut max_del = 0;
    let mut i_list = Vec::new();
    for i in 0..N {
        if max_del.eq(&A[i]) {
            i_list.push(i + 1)
        } else if max_del.lt(&A[i]) {
            i_list.clear();
            max_del = A[i];
            i_list.push(i + 1)
        }
    }
    for i in i_list {
        if B.contains(&i) {
            println!("Yes");
            return;
        }
    }
    println!("No");
}
