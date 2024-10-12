def find_largest(nums: list) :

        largest = nums[0]
        for num in nums:
            if num > largest:
                largest = num

        return largest
numbers = [3, 5, 7, 2, 8, -1, 4]
result = find_largest(numbers)
print(result)
