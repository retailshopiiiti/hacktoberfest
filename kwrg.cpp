#include<bits/stdc++.h>
using namespace std;

#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
template<class T> using indexed_set = tree<T, null_type, less<T>, 
            rb_tree_tag, tree_order_statistics_node_update>;
 
#define ll long long
#define ld long double
#define cy cout<<"YES\n"
#define cn cout<<"NO\n"
#define pii pair<int,int>
 
// 48-57 -> 0-9
// 65-90 -> A-Z
// 97-122 -> a-z
 
bool sortbysec(const pair<ll,ll> &a,const pair<ll,ll> &b)
{ return (a.second < b.second); }
 
ll fastpow(ll a, ll b, ll m)
{
    if(b==0)return 1;
    if(b%2==0){ll take=fastpow(a,b/2,m);return (take*take)%m;}
    else{ll take=fastpow(a,b-1,m);return (a*take)%m;}
}
 
ll ncr(vector<ll> &arr, ll a, ll b, ll mod)
{
    ll ans=(arr[a]*fastpow(arr[b],mod-2,mod))%mod;
    ans=(ans*fastpow(arr[a-b],mod-2,mod))%mod;
    return ans;
}


 
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // freopen("haybales.in", "r", stdin);
    // freopen("haybales.out", "w", stdout);
    int cases=1;
    ll mod=1e9+7;
    cin>>cases;
    // Error can be because you didn't input the entreies
    while(cases--)
    {
        ll n,k;cin>>n>>k;
        ll a[n];
        ll count1=0;
        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]==1)count1++;
        }
        if(count1>0)cy;
        else cn;
    }
    
    // minimise distance in a matkjrix, make a queue with the source and check for adjacent cells
    // max/min problem ?? try to solve using binary search
    // find result in form of mod ?? never use divide operation
    
    return 0;
}











