#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    long long t, i ,j, n, c;
    cin >> t;

    for(i=0; i<t; i++){

        cin >> n;
        c = 0;
        long long ar[n];
        for(j=0; j<n; j++)
            cin >> ar[j];

        for(j=0; j<n; j++){
            if(ar[j] > 1)
                c++;
            if(c == 2)
                break;
        }
        if(c == 2)
            cout << "no" << endl;
        else
            cout << "yes" << endl;
    }

return 0;
}
 //wrong output in codechef
