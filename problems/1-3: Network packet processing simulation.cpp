#include <bits/stdc++.h>

using namespace std;

const int M = 1e5+10;
int S, n, last;
pair<int, int> p[M];
queue<int> buffer;
vector<int> ans;

void deq(int time){
  if (buffer.front() <= time)
    buffer.pop();
}

void request(pair<int, int> packet){
  //cout << buffer.size() << ' ' << S << endl;
  if (buffer.size() < S){
    if (packet.first > last)
      last = packet.first;
    ans.push_back(last);
    buffer.push(last+packet.second);
    last = buffer.back();
  }
  else
    ans.push_back(-1);
}

int main() {
  cin >> S >> n;
  for (int i = 1; i <= n; i++){
    cin >> p[i].first;
    cin >> p[i].second;
  }
  
  last = p[1].first;
  for (int i = 1; i <= n; i++){
    if (!buffer.empty())
      deq(p[i].first);
    request(p[i]);
  }

  for (int i = 0; i < ans.size(); i++)
    cout << ans[i] << endl;

  return 0;
}
