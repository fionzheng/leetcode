class Solution(object):
    def twoSum(self, nums, target):
        hashtable = dict()
      
        for i in range(0, len(nums)):
            difference = target - nums[i]
            if difference in hashtable:
                return[i, hashtable[difference]]
            else:
                hashtable[nums[i]] = i
                
        return None