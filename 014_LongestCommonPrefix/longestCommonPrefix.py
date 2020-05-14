
'''

See Below for original Problem:
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Design
------
- Use a horizontal scan approach. The key is using the all() function to check if a char exists in all strings
- have vars minWord = min(strs, key= len). This will be the focus of determine the lcd since it has the least charcters in it
- have lcd = "" by default
- for loop iterating over minWord
    - utilize the all() function + in check to determine that the minWord[i] is found in all words of array strs
        i.e test = all((minword[i] + lcd) in x for x in strs)  # <-- reads as " The pattern, represented as x. If x is found while iterting through strs, return true"
    - if the test is True
        Then lcd+=minWord[i]

'''

import unittest
import math

# TODO: currently works as an lcd: can find minimum common pattern. But not prefix. Test case of ["ca", "a"] should return "" (no lowestCommonPrefix). Currently returns 'a'

class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        # vars
        minWord = min(strs, key=len) if strs else "" # require minimum word as
        lcp = "" # set lcd as default ""

        # iterate through temp
        for i in range(0, len(minWord)):
            
            # perform a test to check if current lcd + minWord[i] is found in all elements of temp
            charIsPresent = all(lcp + minWord[i] in x for x in strs)
            
            # iterate along minWord charcters, check if in all other words
            if (charIsPresent):
                lcp = lcp + minWord[i]
    
        #print(lcd)
        return lcp  

class SolutionTest(unittest.TestCase):
    def test_01(self):
        result = Solution().longestCommonPrefix(["airflow", "flow","flower", "flows"])
        self.assertEqual(result, "flow")
    
    def test_02(self):
        result = Solution().longestCommonPrefix(["dog","racecar","car"])
        self.assertEqual(result, "")
    
    # an empty list
    def test_03(self):
        result = Solution().longestCommonPrefix([])
        self.assertEqual(result, "")
    
    # common character 'a' exist but not prefix as espected with a 'c'
    def test_03(self):
        result = Solution().longestCommonPrefix(["ca","a"])
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()