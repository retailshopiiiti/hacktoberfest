#include<bits/stdc++.h>
using namespace std;
#include<cstring>
#include<cstdio>
#include<vector>
#include <math.h>

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
 
int power(int a){   
    int ans=0;
    while(a>1)
    { a/=2;ans++; }
    return ans;    
}
 
ll fastpow(ll a, ll b, ll m)
{
    if(b==0)return 1;
    if(b%2==0)
    {
        ll take=fastpow(a,b/2,m);
        return (take*take)%m;
    }
    else
    {
        ll take=fastpow(a,b-1,m);
        return (a*take)%m;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // freopen("haybales.in", "r", stdin);
    // freopen("haybales.out", "w", stdout);
    int cases=1;
    cin>>cases;
    // Error can be because you didn't input the entreies
    while(cases--)
    {
        string a;cin>>a;
        ll n=a.size();
        ll m;cin>>m;
        vector<vector<ll>> arr(9);
        vector<ll> b(n+1,0);
        for(ll i=0;i<n;i++)
        {
            b[i+1]=b[i];
            b[i+1]+=int(a[i]-'0');
            //cout<<b[i+1]<<" ";
        }//cout<<"\n";
        for(ll i=m;i<=n;i++)
        {
            if(arr[(b[i]-b[i-m])%9].size()<2)
            arr[(b[i]-b[i-m])%9].push_back(i-m+1);
        }
        
        
        ll q;cin>>q;
        for(ll i=0;i<q;i++)
        {
            ll l,r,k;
            cin>>l>>r>>k;
            l--;
            ll take=(b[r]-b[l])%9;
            ll ans1=1000000000,ans2=1000000000;
            for(ll j=0;j<9;j++)
            {
                ll it=take*j;
                it%=9;
                ll it1;
                if(it<=k)
                it1=k-it;
                else
                it1=k+9-it;
                ll take1=-1,take2=-1;
                if(it1==j)
                {
                    if(arr[it1].size()>1)
                    {
                        take1=arr[it1][0];
                        take2=arr[it1][1];
                    }
                }
                else
                {
                    if(arr[j].size()>0 && arr[it1].size()>0)
                    {
                        take1=arr[j][0];
                        take2=arr[it1][0];
                    }
                }
                if(take1==-1)continue;
                if(take1<ans1)
                {
                    ans1=take1;
                    ans2=take2;
                }
                if(take2<ans2 && ans1==take1)
                ans2=take2;
            }
            if(ans1==1000000000)
            cout<<"-1 -1"<<"\n";
            else
            cout<<ans1<<" "<<ans2<<"\n";
        }
    }
    
    // minimise distance in a matkjrix, make a queue with the source and check for adjacent cells
    // max/min problem ?? try to solve using binary search
    // find result in form of mod ?? never use divide operation
    
    return 0;
}







