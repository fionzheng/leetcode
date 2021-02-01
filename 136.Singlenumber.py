#class Solution(object):
def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    unique_nums = set(nums) #produces an array of uniquw numbers in nums
    for i in unique_nums:
        count = nums.count(i) #counts the number of times each unique 
        if count == 1:        #number(i) in unique_nums appears in nums
            return i

singleNumber([2,2,1])