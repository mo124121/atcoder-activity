D = int(input())
C = list(map(int, input().split()))
S = [list(map(int, input().split())) for _ in range(D)]
NUM_CONTEST = 26


class Scorer:
    def __init__(self, C, S) -> None:
        self.last = [0] * 26
        self.score = 0
        self.day = 0
        self.C = C
        self.S = S

    def update(self, t, verbose=False):
        t -= 1
        self.score += self.S[self.day][t]
        self.day += 1
        self.last[t] = self.day
        for c, l in zip(self.C, self.last):
            self.score -= c * (self.day - l)
        if verbose:
            print(self.day, self.score)
        return self.score

    def reset(self):
        self.score = 0
        self.day = 0
        self.last = [0] * 26

    def calc_score(self, T, verbose=False):
        self.reset()
        for t in T:
            self.update(t, verbose=verbose)
        if verbose:
            print(*T, self.score)
        return self.score


class EfficientScorer:
    def __init__(self, C, S, init_T) -> None:
        self.total = 0
        self.scores = [0] * NUM_CONTEST
        self.histories = [set() for _ in range(NUM_CONTEST)]
        self.C = C
        self.S = S
        self.T = init_T

        # 操作履歴の初期化
        for d, t in enumerate(self.T):
            t -= 1
            self.histories[t].add(d + 1)

        # コンテストごとにスコアを保持
        for c in range(NUM_CONTEST):
            self.calc_each_score(c)

        # 合計計算
        self.total = sum(self.scores)

    def calc_each_score(self, contest):
        ret = 0
        last = 0
        for d in sorted(self.histories[contest]):
            ret += self.S[d][contest]
            diff = d - last
            ret -= (diff * (diff + 1) // 2) * self.C[contest]
        self.scores[contest] = ret

    def update_T(self, d, q):
        q -= 1
        prev_t = self.T[d - 1]
        prev_score = self.scores[prev_t]


T = []
for d in range(D):
    T.append(int(input()))
M = int(input())
D = [0] * M
Q = [0] * M
for i in range(M):
    D[i], Q[i] = map(int, input().split())

scorer = Scorer(C, S)
for d, q in zip(D, Q):
    T[d - 1] = q
    print(scorer.calc_score(T))
