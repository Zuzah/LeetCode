'''
See:

https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


Walkhtrough
- Testing for condition: .: while looop instead of for loop #< -- Nevermind: Can simply do a simple if in hastack check.
- Test Condition: hatystack[i] === needle
- Output: index of first match: haystack.find(needle)

- IF needle in hastack:
    # once patter known; have to find IndexOf(needle).

ELSE
    return -1

'''

import unittest

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        result: str = "" # house value if pattern is found

        # IF needle is in hastack
        if needle in haystack:
            # return the index of the first found
            result = haystack.find(needle)
            return result 
            
        else:
            return -1

class SolutionTest(unittest.TestCase):
    def test_01(self):
        result = Solution().strStr("hello", "ll")
        self.assertEqual(result, 2, "")

if __name__ == "__main__":
    unittest.main()
