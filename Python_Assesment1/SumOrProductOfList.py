def calculate(nums: list = [], operation= "sum"):
    operation=input("Enter the operation: ")
    if operation == "sum":
        return sum(nums)

    elif operation == "product":
        result = 1
        for num in nums:
            result *= num
        return result
    else:
        print("Choose correct operation: 'sum' or 'product'")


nums = [1, 2, 6]
print(calculate(nums, "sum"))
print(calculate(nums, "product"))
