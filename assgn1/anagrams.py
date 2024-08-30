str1=input("enter the first string: ")
str2=input("enter the second string: ")
dict1={}
dict2={}
for i in range(len(str1)):
    dict1[str1[i]]=str1.count(str1[i])
for i in range(len(str2)):
    dict2[str2[i]]=str2.count(str2[i])

if dict1==dict2:
    print("strings are anagrams")
else:
    print("the strings are not anagrams")
