#include <iostream>
#include <queue>

using namespace std;

int arrmax(int* arr){
    int a;
    for(int i=9;i>0;i--){
        if(arr[i] > 0){
            a = i;
            break;
        }
    }
    return a;
}

int main(){
    int n;
    cin >> n;
    for (int i=0;i<n;i++){
        queue<int> q;
        int m;
        cin >> m;
        int target;
        cin >> target;
        int weightarr[10] = {0,};
        for(int j=0;j<m;j++){
            int weight;
            cin >> weight;
            weightarr[weight]++;
            if (j == target) weight+=10;
            q.push(weight);
        }
        int answer = 0;
        while(1){
            int now = q.front();
            bool time = false;
            if (now>10){
                time = true;
                now-=10;
            }
            int maxWeight = arrmax(weightarr);
            if(now >= maxWeight){
                answer++;
                if (time) break;
                q.pop();
                weightarr[maxWeight]--;
            }else{
                q.pop();
                if (time) now+=10;
                q.push(now);
            }
        }
        cout << answer << "\n";
    }
}
