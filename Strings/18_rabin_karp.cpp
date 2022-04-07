//Time Complexity O(nm) for worst case and O(n+m) for avg and best case. Space Complexity O(1)

#define d 256 
/* pat -> pattern
    txt -> text
    q -> A prime number
*/
void search(char pat[], char txt[], int q){
    int M = strlen(pat);
    int N = strlen(txt);
    int i, j;
    int p = 0; // hash value for pattern
    int t = 0; // hash value for txt
    int h = 1;
    // The value of h would be "pow(d, M-1)%q"
    for (i = 0; i < M - 1; i++)
        h = (h * d) % q;
    // Calculate the hash value of pattern and first
    // window of text
    for (i = 0; i < M; i++){
        p = (d * p + pat[i]) % q;
        t = (d * t + txt[i]) % q;
    }
    for (i = 0; i <= N - M; i++){
        if ( p == t ){  
            bool flag = true;
            for (j = 0; j < M; j++){
                if (txt[i+j] != pat[j])
                {
                  flag = false;
                  break;
                }
                  if(flag)
                  cout<<i<<" ";         
            }
            // if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if (j == M)
                cout<<"Pattern found at index "<< i<<endl;
        }
        // Calculate hash value for next window of text: Remove
        // leading digit, add trailing digit
        if ( i < N-M ){
            t = (d*(t - txt[i]*h) + txt[i+M])%q;
            // We might get negative value of t, converting it
            // to positive
            if (t < 0)
            t = (t + q);
        }
    }
}


//https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/