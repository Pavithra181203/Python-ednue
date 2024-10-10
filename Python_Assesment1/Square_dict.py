def square_dict(nums: list) -> dict:
    result = {}
    for num in nums:
        result[num] = num**2
    return result

print(square_dict([1, 2, 3, 4]))
