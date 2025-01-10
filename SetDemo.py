Set1 = {11,78.89,"Hello",True}

print(Set1)

# print(Set1[1]) ......we cant take indexing in Set

for Value in (Set1):
    
    print(Value)
    
set2 = {11,78,89,11,78} 
print(set2)  

set2.add(101)
print(set2)

set2.remove(101)
print(set2)

print("enter the value in search")

No =int(input())

for value in set2:
    if(No==value):
        
        print("element is present")
        break
