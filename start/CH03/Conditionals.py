#!/usr/bin/env python3
# example workign with conditionals
#By 

answer = input ("Are you happy (y/n)?")
if answer =="y":
    print("you happy")
elif answer =="n":
    print ("not happy")
else:
    print("please answer 'y' or 'no'")


grade = 93

if grade > 95:
    print("A+")

elif grade > 90:
    print("A")

elif grade > 80:
    print("B")

elif grade > 70:
    print("c")
    
    
elif grade > 60:
    print("D")

elif grade < 60:
    print("F")

    print("Done")