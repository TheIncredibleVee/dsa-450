#O(n) expected

def swap(arr, i,j):
    arr[i],arr[j]=arr[j],arr[i]

def partition(arr, l, r,pivot):
    for i in range(l,r):
        if arr[i]==pivot:
            swap(arr, i, r)
            break
    pivot=arr[r]
    i=l
    for j in range(l,r):
        if arr[j]<=pivot:
            swap(arr,i,j)
            i+=1
    swap(arr,i,r)
    return i
        
def findmedian(arr, l ,n):
    lst=sorted(arr[l:l+n])
    return lst[n//2]
def kthSmallest(arr, l, r, k):
    if k>0 and k<=r-l+1:
        n=r-l+1
        
        med=[]
        i=0
        while i<n//5:
            med.append(findmedian(arr,l+i*5,5))
            i+=1
        if i*5<n:
            med.append(findmedian(arr,l+i*5,n%5))
            i+=1
        if i==1:
            medofmedians= med[i-1]
        else:
            medofmedians= kthSmallest(med, 0,i-1,i//2)
        pos=partition(arr,l,r,medofmedians)
        if pos-l==k-1:
            return arr[pos]
        elif pos-l>k-1:
            return kthSmallest(arr,l,pos-1,k)
        else:
            return kthSmallest(arr,pos+1, r, k-pos+l-1)
    return 99999999




#ALternate O(nlogn)
def ALternate(arr,l,r,k):
    arr.sort()
    return arr[k-1]


#https://www.cdn.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-2-expected-linear-time/
#https://www.cdn.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/