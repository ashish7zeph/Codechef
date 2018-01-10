#include <iostream>
using namespace std;

int fact(int  n){
    if(n == 0 || n == 1)
        return 1;
    return n*fact(n-1);
}

int main(){
    int i, n, t;
    cin >> t;
    for(i=0; i<t; i++){
        cin >> n;
        cout << fact(n) << endl;
    }
    return 0;
}
