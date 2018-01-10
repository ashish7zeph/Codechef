#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long long t, i ,j, n, sum;
    cin >> t;

    for(i=0; i<t; i++){

        cin >> n;
        long long ar[n];
        for(j=0; j<n; j++)
            cin >> ar[j];

        sort(ar, ar+n);

        cout << ar[0]*(n-1) << endl;
    }

return 0;
}
