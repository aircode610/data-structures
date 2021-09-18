#include <bits/stdc++.h>

using namespace std;

const int M = 1e5+10;
int n, root;
vector<int> g[M];

int height(int u, int par) {
	int ans = 0;
	for (auto v : g[u]){
		if (v != par)
			ans = max(ans, height(v, u));
	}
	return ++ans;
}

int main() {
	cin >> n;
	for (int u = 0; u < n; u++){
		int v; cin >> v;
		if (v == -1){
			root = u;
			continue;
		}
		g[u].push_back(v);
		g[v].push_back(u);
	}
	cout << height(root, -1) << endl;
	return 0;
}
