#O(n+m)
def merge(self, arr1, arr2, n, m): 
    mx=arr1[0]
    for i in arr1:
        mx=max(i,mx)
    for i in arr2:
        mx=max(i,mx)
    mx+=2
    i=0
    j=0
    k=0
    while i<n and j<m and k<(n+m):
        elem1=arr1[i]%mx
        elem2=arr2[j]%mx
        if elem1<=elem2:
            if k>=n:
                arr2[k-n]+=(elem1*mx)
            else:
                arr1[k]+=(elem1*mx)
            i+=1
        else:
            if k>=n:
                arr2[k-n]+=(elem2*mx)
            else:
                arr1[k]+=(elem2*mx)
            j+=1
        k+=1
    while i<n:
        elem=arr1[i]%mx
        if k>=n:
            arr2[k-n]+=(elem*mx)
        else:
            arr1[k]+=(elem*mx)
        i+=1
        k+=1
    while j<m:
        elem=arr2[j]%mx
        if k>=n:
            arr2[k-n]+=(elem*mx)
        else:
            arr1[k]+=(elem*mx)
        j+=1
        k+=1
    
    for i in range(n):
        arr1[i]=arr1[i]//mx
    for i in range(m):
        arr2[i]=arr2[i]//mx


#Gap method
def merge(arr1, arr2, n, m): 
    gap=(n+m)
    if (gap <= 1):
        gap= 0
    else:
        gap=(gap // 2) + (gap % 2)
    while gap>0:
        i=0
        while (i+gap)<(n+m):
            if i<n:
                if (i+gap)<n:
                    if arr1[i]>arr1[i+gap]:
                        arr1[i], arr1[i+gap]=arr1[i+gap], arr1[i]
                else:
                    if arr1[i]>arr2[i+gap-n]:
                        arr1[i], arr2[i+gap-n]=arr2[i+gap-n], arr1[i]
            else:
                if arr2[i-n]>arr2[i+gap-n]:
                    arr2[i-n], arr2[i+gap-n]= arr2[i+gap-n], arr2[i-n]
            i+=1
        if (gap <= 1):
            gap= 0
        else:
            gap= (gap // 2) + (gap % 2)

#Easy methods >O(n)
#1. comapare 1st elems and swap if required. Then sort the 2dn array(stl or manual insertion sort as only 1st elem is unsorted). repeat till n
#https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/