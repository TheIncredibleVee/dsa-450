int countAvg(vector<int> &v){
    long long sum=0;
    for(auto x:v){
        sum+=x;
    }
    long long avg =  sum/v.size();
    int res=0;
    for(auto x: v){
        if(x==avg){
            res++;
        }
    }
    return res;
}


string findDomain(string domain){
    int i=0;
    while(domain[i]!='@'){              //or we could have used domain.find('@')
        i++;
    }
    return domain.substr(i+1);
}


void email(vector<string> &domains){
    int n=domains.size();
    unordered_map<string, priority_queue<int, vector<int>, greater<int> > > m;
    for(int i=0;i<n;++i){
        string domain=findDomain(domains[i]);
        if(m.find(domain)==m.end()){
            priority_queue<int, vector<int>, greater<int> > pq;
            pq.push(domain[i]);
            m[domain]=pq;
        }else{
            m[domain].push(domain[i]);
        }
    }
    for(auto x:m){
        sendEmail(x.second.top());
    }
}

double avgLargeSmall(vector<int> &v){
    unordered_map<int, int> m;
    int mn=INT_MAX;
    int mx=INT_MIN;
    for(auto x:v){
        mn=min(mn, x);
        mx=max(mx,x);
        m[x]++;
    }
    return (double)(mx*m[mx] + mn*m[mn])/double(m[mx]+m[mn]);
}