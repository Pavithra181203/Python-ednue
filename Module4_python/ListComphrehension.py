# List comprehsension
# simply a looping + condition
# used to filter data & convert list=>dictionary
# syntax:
# listVar =[expression for itemVar in iterable if condition]
# listVar =[expression for itemVar in iterable ]


values=[
    10,
    "abc",
    "100",
    30,
    "XYZ",
    "Axy",
    50,
    50,
]

filteredValues=[]
for value in values:
    if type(value)==int:
        filteredValues.append(value)
print("________normal method____________")
print(filteredValues)

# comprehension method
filteredValues=[value for value in values if type(value)==int]
print("_____________comprehensive method___________")
print(filteredValues)

# to find the occurrence in a list
occurrence = {}
for value in values:
    if not value in occurrence.keys():
        occurrence[value] = 1
    else:
        occurrence[value] += 1
print("*********normal method********")
print(occurrence)



fruits={
    "apple":7,
    "orange":20,
    "grapes":10,
    "pineapple":6,
    "watermelon":3,
    "kiwi":25,
}
lowStockFruits=[fruitName]
