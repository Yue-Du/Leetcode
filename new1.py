def kDifference(a, k):
    # Write your code here
    i=0
    j=0
    output=0
    a_sort=sorted(a)
    while i < len(a):
        if a_sort[i]-a_sort[j]==k:
            output=output+1
            i=i+1
            j=j+1
        elif a_sort[i]-a_sort[j]<k:
            i=i+1
        else:
            j=j+1
    return output





kDifference([1,5,3,4,2],2)