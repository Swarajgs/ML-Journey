def majorityElement(numbers):
    count, candidate = 0, None
    for x in nums:
        if count == 0:
            candidate, count = x, 1
        elif x == candidate:
            count += 1
        else:
            count -= 1
    return candidate                
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))