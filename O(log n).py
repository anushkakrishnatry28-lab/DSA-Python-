def logarithmic(numbers,target):
    left=0
    right=len(numbers)-1
    
    while left <= right:
        mid=(left+right)//2
        
        if numbers[mid]==target:
            return mid
        elif numbers[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
numbers=[2,3,4,5,6,7,8,9,10]
target=int(input("Enter the number:- "))
result=logarithmic(numbers,target)
if result!=-1:
    print("Found at index",result)
else:
    print("Not found")    
            
    
    
 