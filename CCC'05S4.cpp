#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main(){  // todo there is no need for dfs -- it can just be calculated by multiplying actions*10. only do bfs
    ios::sync_with_stdio(false);
    int queries;
    int time_dfs;
    cin >> queries;
    for(int z=0; z<queries; z++){
        vector<string> names;  // todo clear vector so it is reusable for each query
        int calls;
        cin >> calls;
        time_dfs = calls*10;
        for(int i=0; i < calls; i++){
            string call;
            cin >> call;
            names.push_back(call);
        }
        unordered_map<string, vector<string>> network;
        unordered_map<string, bool> visited;
        unordered_map<string, int> depth;
        int max_depth = 1;
        string home = names[calls - 1];
        if(calls==1){
            cout << "0\n";
        }
        else{
            depth[home] = 0;
            if(names[1] != home){
                network[names[0]].push_back(names[1]);
                visited[names[0]] = true;
                depth[names[0]] = 1;
                visited[names[1]] = true;
                depth[names[1]] = 2;
            }
            else{
                network[home].push_back(names[0]);
                visited[names[0]] = true;
                depth[names[0]] = 1;
                visited[home] = true;
            }
            for(int x=2; x<calls-1; x++){  // todo debug multiple occurrences of home
                string current = names[x];
                string prev = names[x-1];
                if(!visited[current]){
                    if(current == home){
                        network[home].push_back(prev);
                        visited[home] = true;
                    }
                    else{
                        network[prev].push_back(current);
                        visited[current] = true;
                        depth[current] = depth[prev]+1;
                        if(depth[current] > max_depth){
                            max_depth = depth[current];
                        }
                    }
                }
            }
        cout << time_dfs - max_depth*20 << "\n";
        }
    }
}