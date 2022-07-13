use std::iter;
struct Fenwick {
    table: Vec<i32>,
}
impl Fenwick {
    pub fn new() -> Self {
        Self { table: vec![0] }
    }
    pub fn push(&mut self, mut x: i32) {
        let n = self.table.len();
        let mut d = 1;
        let k = lsb(n);
        while d != k {
            x += self.table[n - d];
            d *= 2;
        }
        self.table.push(x);
    }
    pub fn prefix_sum(&self, mut i: usize) -> i32 {
        iter::successors(Some(i), |&i| Some(i - lsb(i)))
            .take_while(|&i| i != 0)
            .map(|i| self.table[i])
            .sum()
    }
    pub fn add(&mut self, mut i: usize, x: i32) {
        let n = self.table.len();
        iter::successors(Some(i + 1), |i| Some(*i + lsb(*i)))
            .take_while(|&i| i < n)
            .for_each(|i| self.table[i] += x);
    }
    pub fn from_slice(src: &[i32]) -> Self {
        let mut table = vec![0; src.len() + 1];
        table[1..].copy_from_slice(src);
        let n = table.len();
        (1..n)
            .map(|i| (i, i + lsb(i)))
            .filter(|&(_, j)| j < n)
            .for_each(|(i, j)| table[j] += table[i]);
        Self { table }
    }
}

/*たぶんバグってる */
