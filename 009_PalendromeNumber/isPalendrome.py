
'''
See Below for original Problem:
https://leetcode.com/problems/palindrome-number/

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Design:
1. Convert to a str
- use list comprehension to convert from int to str
- use datatrucutres
    i. strOfX = [] to house list comprehension results
    ii. buffer/reverse = [] will store the reversed list items (if needed)

- algorithm: to take initial temp value. Assign revert= revert * 10 # i.e if 1 then 10 if 10 then 100 <shifts to the left.
                                                revert += temp % 10 place
                                                temp = floor(temp /10)
    while loop: temp originaly set = to x. During processing, temp will be at the end divided by 10. Quit 
    the while loop when temp is divided below 0
        
'''
import unittest
import math

class Solution:
    def isPalindrome_StringConvert(self, x: int) -> bool:
        
        # vars
        strOfX = [] # house list comprehension results
        reverseV1 = [] # a buffer holding the reversed value

        # perform list comprehension to convert x from int to list
        strOfX = [i for i in str(x)]

        # Simple Method to Reverse a List
        reverseV2 = strOfX[::-1] # <-- a slicing trick: [start:end:step]. In this case, from start to end, go every -1 (end to start)

        # Manual Method to Reverse a List
        for i in range(0, len(strOfX)):
            reverseV1+= strOfX[len(strOfX)-1-i]

        if strOfX == reverseV1:
            return True
        else:
            return False

    # Method does not do string convert, uses math operations
    def isPalindrome_NoConvert(self, x: int) -> bool:

        # var to house reversedInt
        temp = x # <--- use temp as it will be later dived and trimmed
        reversed = 0

        # if condition for base cases: if -v or if number does not begin and end in 0
        if (x < 0 or (x % 10 == 0) and x != 0):
            print(False)
            return False

        # while temp var hasn't been completely trimmed less than 0
        while (temp > 0):
            reversed = reversed * 10 # <-- shifts currently calculated reversed var to the left i.e from 4 to 40
            reversed += temp % 10  # <-- appends the next available right most digit of temp var i.e 147 .: 7
            temp = math.floor(temp/10) # <-- trims the original x number by 1 less right most digit i.e 147 .: 14
        
        # if the input mirrors the reversed number (i.e Palendrome)
        if (reversed == x):
            return True
        else:
            return False
        

class isPalindromeTest(unittest.TestCase):

    # Test Cases for Stringify approach to Palendrom
    def test_01(self):
        result = Solution().isPalindrome_StringConvert(121)
        self.assertTrue(result, "Should be True")
    
    def test_02(self):
        result = Solution().isPalindrome_StringConvert(-121)
        self.assertFalse(result, "Should be False")
    
    # Test Cases for math operation only for Palendrome
    def test_03(self):
        result = Solution().isPalindrome_NoConvert(744)
        self.assertFalse(result, "Should be False")
    
    def test_04(self):
        result = Solution().isPalindrome_NoConvert(2112)
        self.assertTrue(result, "Should be True")


if __name__ == "__main__":
    unittest.main()
    #myobj = Solution()
    #myobj.isPalindrome_NoConvert(121)