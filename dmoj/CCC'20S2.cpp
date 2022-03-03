#include <iostream>
#include <queue>
#include <vector>
#include <math.h>
#include <tuple>
using namespace std;
bool visited[1000001];
int arr[1001][1001];

vector<tuple<int, int>> find_factors(int num, int rows, int columns){
    vector<tuple<int, int>> factors;
    for(int i=1; i<int(sqrt(num)+1); i++){
        if(num % i == 0){
            int j = num / i;
            if(i<=rows && j<=columns) {
                tuple<int, int> coords(i, j);
                factors.push_back(coords);
            }
            if(j<=rows && i<=columns){
                tuple<int, int> coords2(j, i);
                factors.push_back(coords2);
            }
        }
    }
    return factors;
}

int main(){
    ios::sync_with_stdio(false);
    int rows, columns, target;
    cin >> rows >> columns;
    target = rows * columns;
    for(int i=1; i<rows+1; i++){
        for(int j=1; j<columns+1; j++){
            cin >> arr[i][j];
        }
    }

    queue<int> q;
    q.push(arr[1][1]);
    while(!q.empty()){
        int c_val = q.front();
        q.pop();
        visited[c_val] = true;
        if(c_val == target){
            cout << "yes";
            return 0;
        }
        vector<tuple<int, int>> factors = find_factors(c_val, rows, columns);
        for(auto factor: factors){
            int val = arr[get<0>(factor)][get<1>(factor)];
            if(!visited[val]){
                q.push(val);
                visited[val] = true;
            }
        }

    }
    cout << "no";
}