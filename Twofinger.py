def remove_duplicatename(name):
    name.sort()
    left=0
    for right in range(1,len(name)):
         if name[left]!=name[right]:
             left=left+1
             name[left]=name[right]
    return left+1
name=["anu","anu","baha","kaha","baha"]
result=remove_duplicatename(name) 
print(name[:result])           
                   