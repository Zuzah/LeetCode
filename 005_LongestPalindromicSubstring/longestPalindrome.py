'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

Example 3:
Input: "cbbc"
Output: "cbbc"

Walkthrough

input = racecar
output = racecar

iterate along the string: for i, chari in enumerate(s):

    # set currentWord = chari   # r

    # for j, jchar in enumerate(s[1:])

        # if j <= lastIndexValue
        currentWord+= charj  #ab ...abb....abbc
        myDictionary[currentWord]=0



Design

'''

import unittest

class Solution:

    def isPalendrome(self, s) -> bool:

        flag: bool

        # iterate along the word
        for i, ichar in enumerate(s):
            # check if the opposite index match up: i -> s[len(s)-i-1]
            if (ichar != s[len(s)-i-1]):
                flag = False
                return flag
        
        return True

    # Brute Force/Too slow for LeetCode acceptance
    def longestPalindromeBruteForce(self, s: str) -> str:
        # vars
        myPalendromes = {}
        flag: bool = True
        largestPalendrome = ""
        currentWord = ""

        # if s empty
        if(s == ""):
            return ""

        for i, ichar in enumerate(s):
            # currentWord starts with the Ith character
            currentWord = ichar
 
            for j, jchar in enumerate(s):

                # IF Jth in betweenthe Ith char and the last char of s: abcda
                if (j> i and j <= len(s)):
                    # then append next available Jth character to create word
                    currentWord+=jchar
 
                    # accept 1st char as a palendrome
                    if(len(currentWord) == 1):
                        myPalendromes[1]=currentWord

                    # utilize helper function to check the current word is a palendrome OR calculate in-place
                    flag = self.isPalendrome(currentWord)
                    
                if (flag != False):
                    myPalendromes[len(currentWord)]= currentWord
        # Print/Test all values in dict()
        #for k, v in myPalendromes.items():
        #    print(v, "=>",k)

        if(myPalendromes):
            largestPalendrome = max(myPalendromes.keys())
        
        return myPalendromes[largestPalendrome]
    

    def longestPalindrome(self, s: str) -> str:
        pass
        


class SolutionTest(unittest.TestCase):

    
    def test01 (self):
        result = Solution().longestPalindromeBruteForce("racecar")
        self.assertEqual(result, "racecar", "Expected Racecar")
    
    
    def test02 (self):
        result = Solution().longestPalindromeBruteForce("")
        self.assertEqual(result, "", "Expected empty")
    
    def test03 (self):
        result = Solution().longestPalindromeBruteForce("a")
        self.assertEqual(result, "a", "Expected a")

    def test04 (self):
        self.lst = ['aba', 'bab']
        result = Solution().longestPalindromeBruteForce("babad")
        self.assertIn(result, self.lst)

    def test05 (self):
        result = Solution().longestPalindromeBruteForce("cbbd")
        self.assertEqual(result, "bb", "Expected bb")
    
    def test06 (self):
        result = Solution().longestPalindromeBruteForce("abcda")
        self.assertEqual(result, "a", "Expected a")
    
    
if __name__ == "__main__":
    unittest.main()

