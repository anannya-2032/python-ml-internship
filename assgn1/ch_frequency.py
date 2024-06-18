str1=input("enter the string: ")
dict={}
for i in range(len(str1)):
    dict[str1[i]]=str1.count(str1[i])
print("the frequency of each letter is : ",dict)