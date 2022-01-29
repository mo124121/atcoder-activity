
#define rep(i,a,b) for(int i=a;i<b;i++)
#define rrep(i,a,b) for(int i=a;i>=b;i--)
#define fore(i,a) for(auto &i:a)
#define all(x) (x).begin(),(x).end()
#pragma GCC optimize ("-O3")
#include<iostream>
using namespace std; void _main(); int main() { cin.tie(0); ios::sync_with_stdio(false); _main(); }
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a = b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a = b; return 1; } return 0; }

int inf=1000000;
int D, G, P[10], C[10];
int dp[11][401010];
//---------------------------------------------------------------------------------------------------
void _main() {
    cin >> D >> G;
    rep(i, 0, D) cin >> P[i] >> C[i];
 
    G /= 100;
    rep(i, 0, D) C[i] /= 100;
 
    rep(i, 0, D + 1) rep(point, 0, 201010) dp[i][point] = inf;
    dp[0][0] = 0;
 
    rep(i, 0, D) rep(point, 0, 201010) {
        rep(j, 0, P[i]) chmin(dp[i + 1][point + (i + 1)*j], dp[i][point] + j);
        chmin(dp[i + 1][point + (i + 1)*P[i] + C[i]], dp[i][point] + P[i]);
    }
 
    int ans = inf;
    rep(point, G, 201010) chmin(ans, dp[D][point]);
    cout << ans << endl;
}