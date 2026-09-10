def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j and numbers[i]==numbers[j]:
                return True
    return False
numbers=[1,3,3,5,5,6]

result=find_duplicates(numbers)
if result:
    print("Duplicate found")
else:
    print("Not found")            