#O(n) and O(n) time and space complexity
def rearrange(arr, n):
    i=0
    pos=[]
    neg=[]
    for i in arr:
        if i>=0:
            pos.append(i);
        else:
            neg.append(i);
    i=0;
    j=0;
    res=[]
    k=0;
    while i<len(pos) and j<len(neg):
        if not k%2:
            res.append(pos[i])
            i+=1
        else:
            res.append(neg[j])
            j+=1
        k+=1
    while i<len(pos):
        res.append(pos[i])
        i+=1
    while j<len(neg):
        res.append(neg[j])
        j+=1
    arr[:]=res

#O(n) and O(1) with rearrange 
#1st move -ve to end(5_move_to_end.py) then just swap with alternate position. Also take i=0, j=1 and loop until i and j<n and swap i and j if one is +e and other is -ve and vice verse is required else i+=1 or j+=1 accordingly. 


#https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/
#https://www.cdn.geeksforgeeks.org/rearrange-array-in-alternating-positive-negative-items-with-o1-extra-space-set-2/
#https://practice.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1#