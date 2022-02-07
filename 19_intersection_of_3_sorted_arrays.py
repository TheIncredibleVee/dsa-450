def commonElements(A, B, C, n1, n2, n3):
    i=0;
    j=0;
    k=0;
    res=[]
    ans=-1
    while i<n1 and j<n2 and k<n3:
        if A[i]==B[j] and B[j]== C[k]:
            if ans==-1 or res[ans]!=A[i]:
                res.append(A[i]);
                ans+=1
            i+=1;
            j+=1;
            k+=1;
        elif A[i]<B[j]:
            if A[i]<C[k]:
                i+=1;
            else:
                k+=1;
        else:
            if B[j]<C[k]:
                j+=1
            else:
                k+=1
    return res;

#Alternate
def commonElements(A, B, C, n1, n2, n3):
    s1=set(A)
    s2= set(B)
    s3=set(C)
    res= s1&s2&s3
    return list(sorted(res))

#https://practice.geeksforgeeks.org/problems/common-elements1132/1#