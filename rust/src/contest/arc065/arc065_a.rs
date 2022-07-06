#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use proconio::input;

fn main() {
    input! {
        mut S:String
    }
    let mut l = S.len();
    let CAND = ["dream", "dreamer", "erase", "eraser"];
    loop {
        for s in CAND.iter() {
            if S.len() < s.len() {
                continue;
            }
            let i = S.len() - s.len();
            if &S[i..] == *s {
                S = S[..i].to_string();
            }
        }
        if S.is_empty() {
            println!("YES");
            return;
        } else if S.len() == l {
            println!("NO");
            return;
        }
        l = S.len();
    }
}
