"""
See Below for original Problem:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

'''
Notes
- list are ALREADY sorted.
- return value is the size of the array, not its contents
- remove in-place, NO extra buffer
- Cannot use for loops since the size of array will be changed each loop
    i.e for i in range(0 )

Walkthrough
[0,0,1,1,1,2,2,3,3,4]

set int i = 0 # will be used to increment through array in while loop; not for loop

while ()
'''

import unittest

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        
        # beginning element index
        i = 0

        # while the index of i is less then the size of nums[] (note: nums size will be shrinking during each loop)
        while (i < len(nums) - 1):

            # if the current number is same as the next number
            if(nums[i] == nums[i+1]):
                del nums[i] # delete item from the list
            else:
                i+=1 # move to the next available cell

        # test results
        #for i in nums:
        #    print(i)

        return len(nums)
    
    def removeDuplicatesAlt(self, nums: [int]) -> int:

        return 0

class TestRemoveReplicats(unittest.TestCase):
    def test_01(self):
        result = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
        self.assertEqual(result,5)

if __name__ == "__main__":
    unittest.main()