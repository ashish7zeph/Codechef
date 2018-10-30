#include<bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define ll long long
#define in insert
#define mod 1000000007
#define vpair vector< pair <ll,ll> >
#define F first
#define S second

ll modexp(ll x, ll y)
{
    ll ans = 1;
    x = x%mod;

    while(y>0){
    if( y % 2 == 1)
        ans = (ans%mod*x%mod)%mod;
    y = y/2;
    x = (x%mod*x%mod)%mod;
    }
    return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    ll int t;
    cin >> t;
    while(t--){

        long long int n,m;
        cin>>n>>m;
        ll int x = n-(m*(m+1)/2);
        ll int a[m], j = 0;
        if(x < 0){
        cout<<"-1"<<endl;
        }
        else{
            ll int  y = (x/m)+1;
            for(ll int j=0; j<m; j++){
                a[j] = y;
                y++;
            }
            ll int z = x % m;
            for(ll int j=m-1; j>=m-z; j--){
                a[j] = a[j]+1;
            }
            ll int sum = 1;
            for(ll int j=0;j<m;j++){
                a[j] = a[j] % mod;
                sum=(sum*((a[j]*(a[j]-1))%mod)%mod)%mod;
                sum=sum%mod;
            }
            cout<<sum<<endl;
        }
    }

}
