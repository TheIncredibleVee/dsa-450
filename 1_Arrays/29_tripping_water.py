def trappingWater(arr,n):
    #O(n) time and O(1) space
    low=0
        high=n-1
        l_max=0
        r_max=0
        res=0
        while(low<=high):
            # l_max=max(arr[low],l_max)
            # r_max=max(arr[high],r_max)
            # res+=max(0,min(l_max,r_max)-min(arr[low],arr[high]))
            # if arr[low]<arr[high]:
            #     low+=1
            # else:
            #     high-=1

            if r_max <= l_max:
                res += max(0, r_max-arr[high])
                r_max = max(r_max, arr[high])
                high -= 1
            else:
                result += max(0, l_max-arr[low])
                l_max = max(l_max, arr[low])
                low += 1
        return res
        
    
    
    
    
    #O(n) time and O(n) space
    # lmax=[0]*n
    # lmax[n-1]=arr[n-1]
    # for i in range(n-2,-1,-1):
    #     lmax[i]=max(lmax[i+1],arr[i])
    # rmax=[0]*n
    # rmax[0]=arr[0]
    # for i in range(1,n):
    #     rmax[i]=max(rmax[i-1],arr[i])
    # res=0
    # for i in range(n):
    #     res+= 0 if arr[i]>min(lmax[i], rmax[i]) else min(lmax[i], rmax[i])-arr[i]
    # return res


    #Using stack
    #O(n) space and O(n) time
    # res=0
    # stack=[]
    # for i in range(n):
    #     while len(stack)!=0 and arr[stack[-1]]<arr[i]:
    #         tp=stack[-1]
    #         stack.pop()
    #         if len(stack)==0:
    #             break
    #         dist=i-stack[-1]-1
    #         height=min(arr[stack[-1]],arr[i])-arr[tp]
    #         res+=dist*height
    #     stack.append(i)
    # return res


#https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1#


    