# check following year leap year or not
"""
created on tue feb 10 2026
@ author : dipak 
"""
year=int(input("enter year:"))
if( year%400==0) or (year%4==0 and year% 100!=0):

    print("Leap Year")
else: 
    print(" not a leap year")
