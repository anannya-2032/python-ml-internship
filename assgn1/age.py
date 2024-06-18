byear=int(input("enter the birth year: "))
cyear=int(input("enter the current year: "))
if(cyear<byear):
    print("invalid input")
else:
    print("age : ", cyear-byear)