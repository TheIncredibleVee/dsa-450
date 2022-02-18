#O(n) time and O(1) space

def threeWayPartition(array,n, a, b):
    low=0
    mid=0
    high=n-1
    while mid<=high:
        if array[mid]<a:
            array[mid] , array[low]=array[low], array[mid]
            mid+=1
            low+=1
        elif array[mid]>=a and array[mid]<=b:
            mid+=1
        else:
            array[mid], array[high]= array[high], array[mid]
            high-=1
	   


# https://practice.geeksforgeeks.org/problems/three-way-partitioning/1#
# https://www.geeksforgeeks.org/three-way-partitioning-of-an-array-around-a-given-range/