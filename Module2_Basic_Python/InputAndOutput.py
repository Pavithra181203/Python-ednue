# input
name=input("Enter your name:")
rollNo=input("Enter your roll no:")
# # output
print(f"My name is {name} and my roll number is {rollNo}")
#
# # to get multiple inputs in single input command
numbers=input("Enter multiple numbers using comma separator:")
commaSeparatedNumber=numbers.split(",")
print(commaSeparatedNumber)

# To check the type of input
test = input("Enter something:")
print(type(test))

# Type conversion/casting

score=input("enter score:")
print(type(score))
print("My HSC score:"+score)
print(100+int(score))


