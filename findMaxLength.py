Contiguous Array
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Solution:
Here we are maintaining the runningsum for each element,if the value is 0 then '-1' if the value is 1 the '-1'
we add them in the dictionary if the runningSum has happened we are calculating the max length that was present,
if not the runningSum is added to the dictionary.
return the MaxLength


time :O(n)
space :O(n)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        maxLength,runningSum = 0,0
        hashMap = {}
        hashMap[0] = -1
        for i in range(len(nums)):
            runningSum =runningSum -1 if nums[i] == 0 else runningSum + 1
            if runningSum not in hashMap:
                hashMap[runningSum] = i
            else:
                maxLength = max(maxLength, i - hashMap[runningSum])
        return maxLength
                
        
        
