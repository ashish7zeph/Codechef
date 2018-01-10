#include <iostream>

#include <algorithm>

using namespace std;



int main(){

	int t, n, k, i, j;

	cin >> t;

	for(i=0; i<t; i++){

		cin >> n >> k;

		int arr[n];

		for(j=0; j<n; j++)

			cin >> arr[j];

		sort(arr, arr+n);

		cout << arr[(n+k)/2] << endl;

	}

return 0;
}
