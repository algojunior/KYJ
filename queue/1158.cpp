#include <iostream>
#include <queue>

using namespace std;
queue<int> q;
int main(){
    int n, k;
    cin >> n;
    cin >> k;
    for(int i = 1;i<=n;i++){
        q.push(i);
    }
    cout << "<";
    while(q.size()!=1){
        for (int j = 0;j<k-1;j++){
            q.push(q.front());
            q.pop();
        }
        cout << q.front() << ", ";
        q.pop();
    }
    cout << q.front() << ">";   
}