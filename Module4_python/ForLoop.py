# names=[
#     "Alex",
#     "Arun",
#     "ajay",
# ]
# for name in names:
#     print(name,end="-")

# Looping a dictionary
fruits={
    "apple":10,
    "grapes":20,
    "orange":30,
}
for fruit in fruits.items():
    print("key is "+fruit[0])
    print("value is "+str(fruit[1]))


# using item dictionary method
for key,value in fruits.items():
    print(f"Count of {key} is {value}")

# using dictionary method-keys() & values
fruitKeys=fruits.keys()
print(fruitKeys)
total=0
for count in fruits.values():
    total+=count
print("Sum of fruits "+str(total))
