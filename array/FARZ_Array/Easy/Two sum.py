def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))

#NOTE: Now we will move to efficent one , for that we will use hashset in which we are storing unvisted index, and we will use target-arr[i] =x and we will chcek if x is prsent in that hashset , if it's we will return arr[i] , and hashset indexes 
def two_sum(nums, target):
    hash_set={}
    for i , num in enumerate(nums):
        compliment = target- num
        if compliment in hash_set:
            return [hash_set[compliment] , i]
        hash_set[num] = i 
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums,target))