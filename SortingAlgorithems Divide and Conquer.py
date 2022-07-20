def insertion_sort(nums):
    nums = list(nums)
    for i in range(len(nums)):
        cur = nums.pop(i)
        j = i-1
        while j >=0 and nums[j] > cur:
            j -= 1
        nums.insert(j+1, cur)
    return nums

a =[1,2,3,4,588,7,4,5,48,6,878,45,8,6]
print(insertion_sort(a))