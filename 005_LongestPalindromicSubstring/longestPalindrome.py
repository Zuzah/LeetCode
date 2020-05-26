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

    # TODO: handle "". 

    # Brute Force/Too slow for LeetCode acceptance
    def longestPalindromeBruteForce(self, s: str) -> str:
        # vars
        myPalendromes = {}
        isPalendrome = False
        largestPalendrome = ""
        currentWord = ""

        # peform 3 nested loops: i head loop over s; j tail loop up to s; k for palendrome validation

        for i, ichar in enumerate(s):
            # currentWord starts with the Ith character
            currentWord = ichar

            # Base Case: allow for the very first char to be considered a palendrome
            if(len(s)>0):
                myPalendromes[s[0]]=1
 
            for j, jchar in enumerate(s):

                # IF Jth in betweenthe Ith char and the last char of s
                if (j> i and j <= len(s)):
                    # then append next available Jth character to create word
                    currentWord+=jchar

                    # iterate over the currentWord and determine IF a palendrome
                    for k, kchar in enumerate(currentWord):
                        
                        # IF the opposite char are not equal
                        if (kchar != currentWord[len(currentWord)-k-1]):
                            isPalendrome = False
                        # ELSE
                        else:
                            isPalendrome = True
                    
                    # IF a Palendrome
                    if(isPalendrome):
                            # insert/overwrite Palendrome into dictionary: key=palendrome, value=length
                            myPalendromes[currentWord]= len(currentWord)
            ## Print/Test all values in dict()
            #for k, v in myPalendromes.items():
            #    print(k, v)

        if(myPalendromes):
            largestPalendrome = max(myPalendromes.keys())
        
        return largestPalendrome
    

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
        result = Solution().longestPalindromeBruteForce("babad")
        self.assertEqual(result, "bab", "Expected bab")
    
    def test05 (self):
        result = Solution().longestPalindromeBruteForce("cbbd")
        self.assertEqual(result, "bb", "Expected bb")
if __name__ == "__main__":
    unittest.main()

