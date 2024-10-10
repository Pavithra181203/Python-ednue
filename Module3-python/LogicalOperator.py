value=int(input("Enter a number:"))
# And operator
if(value>=40) and (value<=60):
    print("Entered number is in range")
# Or operator
if(value==0) or (value==1):
    print("Entered number is binary")
# Not operator
if not(value==1):
    print("the number is not 1")

# Method1
if(value>=40) and (value<=50):
    print("The number is between 40 and 50")
elif(value>=80) and (value<=90):
    print("The number is between 80 and 90")

# Method2
if((value>=40) and (value<=50)) or ((value>=80) and (value<=90)):
    print("the number is between 40 and 50 ")
