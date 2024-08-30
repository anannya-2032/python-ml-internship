'''str1=input("enter the string: ")
lst1=[]
for i in range(len(str1)):
    lst1.append(str1[i])
print("list of characters: ", lst1)'''

l=[1,2,3,4,5]
s=set(l)
l.append(6)
print(l,s)