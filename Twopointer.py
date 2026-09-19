def find_two_numbers(number,target):
    left=0
    right=len(number)-1
    while left<right:
        sum=number[left]+number[right]
        if sum==target:
            print(number[left],number[right])
            break
        elif sum>target:
            right-=1
        else:
            left-=1
    return -1
number=[1,2,3,4,5,6,7,8,11]
target=int(input("Enter the number:- ")) 
result=find_two_numbers(number,target)
if result:
    print("Number found")
else:
    print("Number not found")    
    
                          
    