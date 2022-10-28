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
    ll mod=998244353;
    cin>>cases;
    // Error can be because you didn't input the entreies
    while(cases--)
    {
        ll n;cin>>n;
        ll a[n];
        ll count1=0,count=0;
        for(ll i=0;i<n;i++)
        {
            cin>>a[i];
            if(a[i]==1)
            count1++;
            else
            count++;
        }
        if(count==count1)
        {
            cout<<n<<"\n";
            for(ll i=1;i<=n;i++)
            cout<<i<<" "<<i<<"\n";
        }
        else if(count1>count)
        {
            vector<pair<int,int>> it;
            it.push_back({1,1});
            for(ll i=1;i<n;i++)
            {
                if(a[i]==1 && a[i-1]==1 && it.back().first==it.back().second && count1>count)
                {
                    it.pop_back();
                    it.push_back({i,i+1});
                    count1-=2;
                }
                else
                it.push_back({i+1,i+1});
            }
            ll ans=0;
            for(auto x:it)
            {
                if(x.first==x.second)
                ans+=a[x.first-1];
                // cout<<x.first<<"/"<<x.second<<" ";
            }
            if(ans!=0)cout<<"-1";
            else
            {
                cout<<it.size()<<"\n";
                for(auto x:it)
                cout<<x.first<<" "<<x.second<<"\n";
            }
        }
        else
        {
            vector<pair<int,int>> it;
            it.push_back({1,1});
            for(ll i=1;i<n;i++)
            {
                if(a[i]==-1 && a[i-1]==-1 && it.back().first==it.back().second && count>count1)
                {
                    it.pop_back();
                    it.push_back({i,i+1});
                    count-=2;
                }
                else
                it.push_back({i+1,i+1});
            }
            ll ans=0;
            for(auto x:it)
            {
                if(x.first==x.second)
                ans+=a[x.first-1];
            }
            if(ans!=0)cout<<"-1";
            else
            {
                cout<<it.size()<<"\n";
                for(auto x:it)
                cout<<x.first<<" "<<x.second<<"\n";
            }
        }
        cout<<"\n";
    }
    
    // minimise distance in a matkjrix, make a queue with the source and check for adjacent cells
    // max/min problem ?? try to solve using binary search
    // find result in form of mod ?? never use divide operation
    
    return 0;
}











