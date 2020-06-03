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
    
    '''
    aaaa

    isEven
        .: No midpoint to calculate
        left = 
    '''

    def longestPalindrome(self, s: str) -> str:
        # vars
        myPalendromes = {}
        largestPalendrome: int = 0
        midpoint: int
        leftTuple: int
        rightTuple: int
        left: int
        right: int
        isEvenLength = True if len(s) % 2 == 0 else False # character length of odd and even important in palendromes
        
        # Basecase: if s is empty
        if (len(s) == 0):
            return ""
  
        # if the string char # are event i.e 'aa' or 'aaaa'. Len = 2 or 4. .: tuples - 2/2=1 and 4/2=2. Tuples are 
        if(isEvenLength == True):
            # determine the tuple chars
            leftTuple = s[int(len(s)/2)-1]
            rightTuple = s[int(len(s)/2)]
            
            # push just the left tuple as a palendrome
            myPalendromes[len(leftTuple)]=leftTuple

            # if both tuples are palendrome
            if(leftTuple == rightTuple):
                currentWord = leftTuple + rightTuple
                myPalendromes[len(currentWord)]=currentWord
            left = int(len(s)/2) -1 -1
            right = int(len(s)/2) + 1
    

        # 'aaa' or 'aaaaa' midpoint = 3/2=1.5 or 5/2=2.5
        if(isEvenLength == False):
            # determine the midpoint chars
            # set left and right vars to
                  # determine the tuple chars
            midpoint = int(len(s)/2)
            currentWord = s[midpoint]
            left = midpoint -1
            right = midpoint + 1
            myPalendromes[len(currentWord)]=currentWord
            
        # while left and right pointers not pass boundries: racecar midpoint a, therefore
        while (left >= 0 and right <= len(s)-1 and s[left] == s[right]):

            currentWord= s[left] + currentWord + s[right]
            myPalendromes[len(currentWord)]=currentWord
            left-=1
            right+=1
            
        # claculate largest key() value in dictionary
        largestPalendrome = max(myPalendromes.keys())
    
        # test dict values
        for k, v in myPalendromes.items():
            print (k, v)

        return myPalendromes[largestPalendrome]

class SolutionTest(unittest.TestCase):

    
    def test01 (self):
        result = Solution().longestPalindrome("racecar")
        self.assertEqual(result, "racecar", "Expected Racecar")
    
    
    def test02 (self):
        result = Solution().longestPalindrome("")
        self.assertEqual(result, "", "Expected empty")
    
    def test03 (self):
        result = Solution().longestPalindrome("a")
        self.assertEqual(result, "a", "Expected a")
    
    def test04 (self):
        self.lst = ['aba', 'bab']
        result = Solution().longestPalindrome("babad")
        self.assertIn(result, self.lst)
    
    
    def test05 (self):
        result = Solution().longestPalindrome("cbbd")
        self.assertEqual(result, "bb", "Expected bb")
    
    def test06 (self):
        self.lst = ['a,','c']
        result = Solution().longestPalindrome("abcda")
        self.assertIn(result, self.lst)
    
    def test06 (self):
        self.lst = ['a','c']
        result = Solution().longestPalindrome("ac")
        self.assertIn(result, self.lst)
    
    def test07 (self):
        result = Solution().longestPalindrome("abb")
        self.assertEqual(result, "bb", "Expected bb")
    
    
if __name__ == "__main__":
    unittest.main()
    #myObj = Solution()
    #myObj.longestPalindrome("eeee")
