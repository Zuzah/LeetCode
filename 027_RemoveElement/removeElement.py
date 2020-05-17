

'''
https://leetcode.com/problems/remove-element/

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Walkthrough
- iterate through the end of the array
    while (i < len(nums)-1):


- at index i, check if == val.
    del nums[i] 
else:
    i=+1

return len(nums)


Design
var i = 0
while loop( i < len(nums)) #< -- not len() -1

if nums[i] == val
  delete object from list

else: move along
    i+=1
''''

import unittest

class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        
        # vars
        i = 0 #<-- used in while loop

        # loop through end of nums
        # for i in range(0, len(nums)-1):
        while (i < len(nums)):
            
            # if nums[i] == val
            if(nums[i] == val):
                # del nums[i]
                del nums[i]
            
            # else: along index
            else:
                i+=1
        #for i in nums:
        #    print(i)
        return len(nums)

class TestSolution(unittest.TestCase):
    def test_01(self):
        result = Solution().removeElement([3,2,2,3], 3)
        self.assertEquals(result, 2, "")
    
    def test_02(self):
        result = Solution().removeElement([0,1,2,2,3,0,4,2], 2)
        self.assertEquals(result, 5, "")

if (__name__ == "__main__"):
    unittest.main()