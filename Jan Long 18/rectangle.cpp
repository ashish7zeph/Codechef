#include <iostream>
#include <algorithm>
using namespace std;

int main(){

    long i, t, j, a[4];
    cin >> t;
    for(i=0; i<t; i++){

        for(j=0; j<4; j++)
            cin >> a[j];
        sort(a, a+4);
        if((a[0] == a[1]) && (a[2] == a[3]))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}