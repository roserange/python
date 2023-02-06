def solve(nums):
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                count+=1
    return count

nums=[1,1,1,7,9,8]
print(solve(nums))
