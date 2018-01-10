#include <iostream>
using namespace std;

int main(){
    long long t, i ,j, n, sum;
    cin >> t;
    for(i=0; i<t; i++){
        cin >> n;
        sum = 0;
        while(n){
            sum += (n % 10);
            n /= 10;
        }
        cout << sum << endl;
    }
return 0;
}
