#include <iostream>
using namespace std;

int main(){
    long a, t, i, n;9
    cin >> t;
    for(i=0; i<t; i++){
        cin >> n;
        a = n%10;
        while(n%10 != n){
            n = n/10;
        }
        cout << a+n << endl;
    }
    return 0;
}
