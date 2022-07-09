#![allow(clippy::let_unit_value)]
#![allow(non_snake_case)]
use std::collections::HashMap;

use proconio::input;

struct ExpDP {
    m: HashMap<(usize, usize, usize), f64>,
}
impl ExpDP {
    fn solve(a: usize, b: usize, c: usize) -> f64 {
        ExpDP { m: HashMap::new() }.rec(a, b, c)
    }

    fn rec(&mut self, a: usize, b: usize, c: usize) -> f64 {
        if self.m.contains_key(&(a, b, c)) {
            return self.m[&(a, b, c)];
        }
        if a == 100 || b == 100 || c == 100 {
            return 0_f64;
        }
        let mut ret = 0_f64;
        let z = a as f64 + b as f64 + c as f64;
        if a != 0 {
            ret += a as f64 / z * self.rec(a + 1, b, c);
        }
        if b != 0 {
            ret += b as f64 / z * self.rec(a, b + 1, c);
        }
        if c != 0 {
            ret += c as f64 / z * self.rec(a, b, c + 1);
        }

        self.m.insert((a, b, c), ret + 1.0);

        ret + 1.0
    }
}

fn main() {
    input! {
        A:usize,
        B:usize,
        C:usize
    }
    let ret = ExpDP::solve(A, B, C);
    println!("{:.10}", ret)
}
