
'''
Walkthrough
objective: return location of first non-repeat cahr.
- iterate along the string: "ccc", "leetcodelove"
- at current char i, if founder later in string (s[i+1:end])

Design
'''

import unittest
import collections

class Solution:
    def firstUniqCharBruteForce(self, s: str) -> int:

        repeatDict = {}

        for idx, char in enumerate(s):

            if (repeatDict.get(char) == None):
                repeatDict[char]= False
            else:
                repeatDict[char] = True

            if (char not in s[idx+1: len(s)] and repeatDict[char]== False):
                return idx

        return -1
    
    # solution from Leetcode. Is faster by 200ms above the above BruteForce
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int

        Time Complexity: O(n) since we go trhough string of length N two times

        Space Complexity: O(1) because english alphabet contains 26 chars
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1


class Test(unittest.TestCase):
    def test_01(self):
        result = Solution().firstUniqCharBruteForce("loveleetcode")
        self.assertEqual(result, 2, "Should be 2: where letter v is")
    
    def test_02(self):
        result = Solution().firstUniqChar("")
        self.assertEqual(result, -1, "No char's so -1")

    def test_03(self):
        result = Solution().firstUniqChar("ccc")
        self.assertEqual(result, -1, "All strings here are repeated")

if __name__ == "__main__":
    unittest.main()
        