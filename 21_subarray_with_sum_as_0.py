def subArrayExists(arr,n):
    ##Your code here
    #Return true or false
    presum={};
    temp=0;
    for i in arr:
        if i==0:
            return True;
        if i+temp in presum or i+temp==0:
            return True;
        presum[i+temp]=1
        temp+=i;
    return False;


#https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
#https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/