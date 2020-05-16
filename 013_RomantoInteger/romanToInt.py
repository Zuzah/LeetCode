"""
See Below for original Problem:
https://leetcode.com/problems/roman-to-integer/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the 
number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine,
which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Notes
- There are seven different symbols, each with a value
    i.e Dictionary = {'I':'i', 'X':'10'}

- All numeberals are added together, with exception of 6 cases where subtraction is peformed
    if result = 4 or 9 .: preceed with an "I"
    if 40 or 90 .: proceed with an "L" i.e 39 

- the KEY to remember to examine previous numberal agains current numberal. 
    IF the previous numberal was larger than the current i.e prev = V, current= I
        THEN just add them to result: result += current
    
    ELSE if previous numberal was smaller than the current i.e prev = I, current = V
        THEN undo the previous entered value from result
            result = result - previous
            and then replace with the calculation: current - prev
            i.e result+ = (current - previous)

            Consolidation this is:
            result+ = (current - previous) - previous


"""

import unittest


class Solution:

    # Solution provied from another user on LeetCode
    # https://leetcode.com/problems/roman-to-integer/discuss/633714/Runtime%3A-28-ms-faster-than-99.81-of-Python3-online-submissions-for-Roman-to-Integer.
    def romanToIntV2(self, s: str) -> int:
        romanDictionary = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        previousNumberal = 1000 # by default, set the previousNumberal as the max possible: M

        # iterate to the end of the roman number
        for i in range(0, len(s)):
            # set var to current numberal being processed
            currentNumberal = romanDictionary[s[i]]
            
            # if the current roman numberal is less <= to the previous Numberal i.e VI
            if currentNumberal <= previousNumberal:
                # then add the sums as normal
                result = result + currentNumberal
            else:
                # re-caculate result by removing the entry of the previousNumberal. And the replace with current - previousNumberal
                result = result + (currentNumberal - previousNumberal) - previousNumberal
            
            # set the currentNumberal as now the previousNumberal for use in the next loop
            previousNumberal = currentNumberal
        #print(result)
        return result


class SolutionsTest(unittest.TestCase):
    def test01(self):
        result = Solution().romanToIntV2("CDLIX")
        self.assertEquals(result, 459, "Value should be 459")
    
    def test02(self):
        result = Solution().romanToIntV2("LVIII")
        self.assertEquals(result, 58, "Value should be 58")


if __name__ == "__main__":
    unittest.main()
