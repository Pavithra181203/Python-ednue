# Method1=>Numbers of arguments
def addition(num1,num2):
    sum=num1+num2
    return sum
print (addition(10,20))

# method2=>keyword argument
def addition(num2,num1):
    sum=num1+num2
    return sum
result2=addition(num1=10,num2=20)
print(result2)

# method 3=>arbitrary arguments(*args)
def addition(*nums):
    return sum(nums)# using python build in method-sum()
result3=addition(10,20,30,40)
print(result3)
result4=addition(10,20,30,40,50)
print(result4)
result5=addition() # without passing an argument the result will be 0
print(result5)

method4=>keyword arbitrary arguments(**kwargs)
def addition(num2,num1):
    sum=num1+num2
    return sum





