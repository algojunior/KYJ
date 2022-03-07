#include<iostream>

using namespace std;

struct Queue{
    int arr[2000000];
    int begin, end;
    Queue(){
        begin = 0;
        end = 0;
    }
    
    void push(int a){
        arr[end] = a;
        end++;
    }
    
    bool empty(){
        if (end == begin) return 1;
        else return 0;
    }
    
    int pop(){
        if(empty()) return -1;
        else{
            begin++;
            return arr[begin-1];
        }
    }
    
    int size(){
        return end - begin;
    }
    
    int front(){
        if(empty()) return -1;
        else return arr[begin];
    }
    
    int back(){
        if(empty()) return -1;
        else return arr[end-1];
    }
};

int main(){
    cin.tie(0);
    cin.sync_with_stdio(0);
    int n;
    cin >> n;
    Queue q;
    while(n--){
        string cmd;
        cin >> cmd;
        if(cmd == "push"){
            int num;
            cin >> num;
            q.push(num);
        }
        else if(cmd == "pop"){
            cout << q.pop() << "\n";
        }
        else if(cmd == "size"){
            cout << q.size() << "\n";
        }
        else if(cmd == "empty"){
            if(q.empty()) cout << "1" << "\n";
            else cout << "0" << "\n";
        }
        else if(cmd == "front"){
            cout << q.front() << "\n";
        }else if(cmd == "back"){
            cout << q.back() << "\n";
            
        }
    }
}

