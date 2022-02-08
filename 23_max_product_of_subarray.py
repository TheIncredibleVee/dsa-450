def maxProduct(arr, n):
    mini=maxi=arr[0]
    res=arr[0];
    for i, val in enumerate(arr):
        if i==0:
            continue
        if val<0:
            mini, maxi=maxi,mini
        mini=min(mini*val, val)
        maxi=max(maxi*val, val)
        res=max(res, maxi)
    return res


#alternate C++ implementation

# int maxSubarrayProduct(int arr[], int n)
# {
# 	int max_ending_here = arr[0];

# 	int min_ending_here = arr[0];

# 	int max_so_far = arr[0];
# 	
# 	for (int i = 1; i < n; i++)
# 	{
# 		int temp = max({arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here});
# 		min_ending_here = min({arr[i], arr[i] * max_ending_here, arr[i] * min_ending_here});
# 		max_ending_here = temp;
# 		max_so_far = max(max_so_far, max_ending_here);
# 	}
# 	return max_so_far;
# }



#https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1
#https://www.geeksforgeeks.org/maximum-product-subarray/
#https://www.geeksforgeeks.org/maximum-product-subarray-set-2-using-two-traversals/