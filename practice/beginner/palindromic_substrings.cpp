#include <iostream>
using namespace std;

int main(){
    int i, t, j, c, k;
    string s1, s2;
    cin >> t;
    for(i=0; i<t; i++){
        cin >> s1 >> s2;
        c = 0;
        for(j=0; j<s1.size(); j++){
            for(k=0; k<s2.size(); k++){
                if(s1[j] == s2[k]){
                    c = 1;
                    break;
                }
            }
        }
        if(c == 1)
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }
    return 0;
}
