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

    def longestPalindromeUgly(self, s: str) -> str:
        # vars
        myPalendromes = {} #len(word), palenddrome
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

    '''
    Walkthrough:
    s = racecar

    - iterate along the string
    - at each index i (i=0 is 'r')
        - while (left >=0, right< len(s)):
            - chick if left/right cars are equal (at beggining, both point to i[0])
                if equal and if value > largestPalendrome
                
    '''

    def longestPalindromeBetter(self, s: str) -> str:
        '''
        Approach: "expand around center" where centre is relative as you iterate along the array
            i.e = s = 'racecar'
            r | a | c | e | c | a | r

            a | a | a | a

        Requirments
        - left =0, right = 0
        - largestPalendrome = ""
        - flag for isEven: isEvengt = True if len(s) % 2 == 0 else False
        - while loop (left >=0 and right<len(s)):
            if (s[left] == s[right]):
                left-+1
                right+=1
            else:
                break
            
            currentWord = s[left:right] #if odd?

            largestPalendrom = currentWord if len(currentWord) > largestPalendrome else largestPalendrom

        '''
        leftIndex = 0
        rightIndex = 0
        left: int = 0
        right: int = 0
        currentWord = ""
        center = 0
        largestPalendrome = ""
        isEven = True if len(s) % 2 == 0 else False

        # test: abbc
        for i, ichar in enumerate(s):
            left = i
            right = i
            leftIndex = 0
            rightIndex = 0
            while (left >=0 and right < len(s)):
                if (s[left] == s[right]):
                    leftIndex = left
                    rightIndex = right
                else:
                    break
                left-=1
                right+=1
            currentWord = s[leftIndex: rightIndex+1]
            print(currentWord)

            if (len(currentWord) > len(largestPalendrome)):
                largestPalendrome = currentWord

        return largestPalendrome


        

    def longestPalindrome(self, s: str) -> str:

        #need two method: helpder and longest palnedrom
        # must consider cases if the substring is even or odd length
        # must approach as relative to index: start at index -0. Check left, right pointesrs. if s[index]

        '''
        - odd/even check
        'relative midpoint' -> iterate through s. check adjacent next cell (i+1). If exists, and IF ==, then even: get tuple. IF exists and not equal, odd: get midpoint
            Case1: "racecar" -> r. midpoint = 0. left = 0, right=2. No, so next itera
                                ra. midpoint = 1. left = 0, right = 2. len = 3. Not palendrome, 
                                rac
        '''

        #vars: racecar
        # raabbaacar
        # calculate for odd palindrome
        # for i in range(len(s)):
        #   midpoint = i
        #   len = 1
        #   left = i - 1
        #   right = i + 1
        #   while (left >= 0 and right < len(s) && s[left] == s[right]):
        #     len += 2
        #     left -= 1
        #     right += 1

         # calculate for even palindrome
        # for i in range(len(s)):
        #   midpoint = i
        #   if (s[midpoint] == s[midpoint + 1]):
        #   len = 2
        #   left = midpoint - 1
        #   right = midpoint + 2
        #   while (left >= 0 and right < len(s) && s[left] == s[right]):
        #     len += 2
        #     left -= 1
        #     right += 1
        

        pass

class SolutionTest(unittest.TestCase):

    # Test Cases for odd length strings
    '''
    def test01 (self):
        result = Solution().longestPalindromeBetter("racecar")
        self.assertEqual(result, "racecar", "Expected Racecar")

    def test03 (self):
        result = Solution().longestPalindromeBetter("a")
        self.assertEqual(result, "a", "Expected a")
    
    def test04 (self):
        self.lst = ['aba', 'bab']
        result = Solution().longestPalindromeBetter("babad")
        self.assertIn(result, self.lst)
    
    def test06 (self):
        self.lst = ['a','c']
        result = Solution().longestPalindromeBetter("abcda")
        self.assertIn(result, self.lst)
    '''
    def test07 (self):
        result = Solution().longestPalindromeBetter("abbc")
        self.assertEqual(result, "bb", "Expected bb")
    '''
    def test02 (self):
        result = Solution().longestPalindrome("")
        self.assertEqual(result, "", "Expected empty")

    
   
    def test05 (self):
        result = Solution().longestPalindrome("cbbd")
        self.assertEqual(result, "bb", "Expected bb")
    

    
    def test06 (self):
        self.lst = ['a','c']
        result = Solution().longestPalindrome("ac")
        self.assertIn(result, self.lst)
    

    
    '''
if __name__ == "__main__":
    unittest.main()
    #myObj = Solution()
    #myObj.longestPalindrome("eeee")
