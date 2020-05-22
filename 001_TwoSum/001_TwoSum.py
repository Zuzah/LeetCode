'''
See Below for original Problem:
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:

      
        # There are 2 algorithms to utilize below: OnePassHash and BruteForce Method. Swap in one of the two methods into the main call below
        

        # ====== One pass hash closure to solve problem ======
        '''
        Strategy: utilize a Dictionary to house numbers and index they were found in the array i.e Dictionary[nums[i], i]
                - Set a compliments variable (compliment = target - nums[i])
                - If the compliment for nums[i] to make the sum is IN the dictionary, then return [compliment, i]
                - Else, add current nums[i] to the Dictionary
        Time Complexity: O(n) as just 1 loop, and dictionaries take O(1) time to access
        Space Complexity: O(n) as the Dictionary would be the max size of input
        '''
        def onePassHash(self, nums: [int], target: int) -> [int]:

            #create dictionary to store key/values of: [nums[i], i]
            complimentHash: dict = {} 

            # iterate through the nums
            for i, number in enumerate(nums):

                # calculate compliment value to achieve target on i
                compliment = target - number

                # if compliment is in hashtable.value 
                if compliment in complimentHash:
                    # return indices of the compliment, and index i
                    return [complimentHash[compliment], i]
                
                else:
                    complimentHash[number]=i
            
            return [0]
        
        # ====== Bruteforce closure to solve problem ======
        '''
        Strategy: Use to loops to iterate: head and tail loop. Compare i+ j=target where i<j
        TimeComplexity: O(n2) - two loops that iterate through n
        Space Compexity: O(1) as not storage is performed, simply read, calculation, and output
        '''
        def bruteForce(self, nums: [int], target: int) -> [int]:

            # iterate over the array (head loop)
            for i in range(0, len(nums)):
                # iterate over the array (tail loop), starting at i+1
                for j in range(i+1, len(nums)):
                    # if the sum of the locations at i a j equals target
                    if (nums[i] + nums[j] == target):
                        # then return the indices of the pair thats generates the sum value
                        return [i, j]
            
            return [0]

        # swap in one of the above closures to solve the Sum of Two numbers problem
        result = onePassHash(self,nums, target)

        return result

# main method
if __name__ == "__main__":
    myObj = Solution()
    print(myObj.twoSum([2, 7, 11, 15],13))