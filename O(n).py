def find_name(names,target):
    for i in names:
        if i==target:
            return True
        return False
names=["anu","jak","bubsdu","sniasd","dibais"]
target=input("Enter the names:- ")
result=find_name(names,target)
if result:
    print("Name found")
    
else:
    print("Not found")    
