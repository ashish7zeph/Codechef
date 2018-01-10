#include <iostream>
using namespace std;

int main(){

    long long t, n, p, i, j, cake, hard;

    cin >> t;
    for(i=0; i<t; i++){

        cin >> n >> p;
        int ar[n];
        cake = 0;
        hard = 0;

        for(j=0; j<n; j++){
            cin >> ar[j];
            if( ar[j] <= p/10 )
                hard++;
            if( ar[j] >= p/2 )
                cake++;
        }
        if(hard == 2 && cake == 1)
            cout << "yes" << endl;
        else
            cout << "no" << endl;
    }
    return 0;
}
