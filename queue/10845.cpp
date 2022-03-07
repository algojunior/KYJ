#include<iostream>

using namespace std;

struct Queue
{
    int arr[10000];
    int begin, end;

    Queue(){
        begin = 0;
        end = 0;
    }

    void push(int a){
        arr[end] = a;
        end++;
    }

    int pop(){
        if (begin == end){
            return -1;
        }else{
            begin++;
            return arr[begin-1];
        }
    }

    int size(){
        return end - begin;
    }

    bool empty(){
        if (begin == end){
            return true;
        }else{
            return false;
        }
    }

    int front(){
        if (empty()){
            return -1;
        }else{
            return arr[begin];
        }
    }

    int back(){
        if (empty()){
            return -1;
        }else{
            return arr[end-1];
        }
    }
    /* data */
};

int main(){
    ios::sync_with_stdio(false);

    int n;
    cin >> n;

    Queue q;

    for(int i = 0;i<n;i++){
        string commend;
        cin >> commend;
        if (commend == "push"){
            int num;
            cin >> num;
            q.push(num);
        }else if(commend == "pop"){
            cout << q.pop() << "\n";
        }else if(commend == "size"){
            cout << q.size() << "\n";
        }else if(commend == "empty"){
            if(q.empty()) cout << "1" << "\n";
            else cout << "0" << "\n";
        }else if(commend == "front"){
            cout << q.front() << "\n";
        }else if(commend == "back"){
            cout << q.back() << "\n";
        }
    }
}
