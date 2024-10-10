# dict comprehsension
# simply a looping + condition
# used to filter data & convert list=>dictionary
# syntax:
# listVar ={keyexpression: valueExpression for itemVar in iterable if condition}

fruits={
    "apple":7,
    "orange":20,
    "grapes":10,
    "pineapple":6,
    "watermelon":3,
    "kiwi":25,
}
orderCount = {fruitName: 10-stockCount for fruitName,stockCount in fruits.items() if stockCount < 10}
print(orderCount)
