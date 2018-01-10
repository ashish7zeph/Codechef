#include <iostream>
#include <string>
using namespace std;

int main(){
    int i, t, j, space, c;
    string name;
    cin >> t;
    for(i=0; i<t; i++){

        space = 0;
        c = 0;
        getline(cin >> ws, name);

        for(j=0; j<name.size(); j++){
            if(name[j] == ' ')
                space++;
        }
        if(space == 0){
            cout << char(toupper(name[0]));

            for(j=1; j<name.size(); j++)
                cout << char(tolower(name[j]));
        }
        else if(space > 0){
            cout << char(toupper(name[0])) << ". ";

            for(j=0; j<name.size(); j++){
                if(name[j] == ' ' && space > 1){
                    cout << char(toupper(name[j+1])) << ". ";
                    space--;
                }
                else if(space == 1 && name[j] == ' ' && c == 0){
                    cout << char(toupper(name[j+1]));
                    c = 1;
                    j++;
                    space--;
                }
                else if(c == 1)
                    cout << char(tolower(name[j]));
            }
        }
        cout << endl;
    }
    return 0;
}
