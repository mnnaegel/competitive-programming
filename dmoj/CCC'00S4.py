#include <bits/stdc++.h>
using namespace std;

int solve(int amount, vector<int> clubs){
    int dp[5281];
    for(int i=0; i<5281; i++){
        dp[i] = INT_MAX-1;
    }
    dp[0] = 0;
    for(auto club: clubs){
        for(int i=club; i<=amount; i++){
            dp[i] = min(dp[i], dp[i-club]+1);
        }
    }
    return dp[amount];
}

int main(){
    int amount, c;
    cin >> amount >> c;
    vector<int> clubs;
    for(int i=0; i<c; i++){
        int elem;
        cin >> elem;
        clubs.push_back(elem);
    }
    sort(clubs.begin(), clubs.end());
    int result = solve(amount, clubs);
    if(result < 5280){
        cout << "Roberta wins in " << result << " strokes.";
    }
    else{
        cout << "Roberta acknowledges defeat.";
    }
}