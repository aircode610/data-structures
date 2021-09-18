#include <bits/stdc++.h>

using namespace std;

map <char, char> match = {
	{'}', '{'},
	{']', '['},
	{')', '('}
};

int main() {
	vector<pair<char, int> > stack;
	string str;
	cin >> str;
	str = '-'+str;
	for (int i = 1; i < str.size(); i++){
		//push open brackets
		if (str[i] == '{' || str[i] == '[' || str[i] == '(')
			stack.push_back({str[i], i});
		//check close brackets
		else if (str[i] == '}' || str[i] == ']' || str[i] == ')'){
			//check if empty
			if (stack.empty()){
				cout << i << endl;
				return 0;
			}
			//check if match
			if (stack.back().first == match[str[i]])
				stack.pop_back();
			else {
				cout << i << endl;
				return 0;
			}
		}
	}
	//check if empty
	if (stack.empty())
		cout << "Success" << endl;
	else
		cout << stack[0].second << endl;

	return 0;
}

/*
push open brackets *
check close brackets *
*/
