"""
Difficulty: Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note:

    All inputs will be in lowercase.
    The order of your output does not matter.

"""

from typing import List
import unittest
import collections

class Solution:
    # the following was first attemp on own. It would be O(n2) time complexity
    def groupAnagramsBruteForce(self, strs: List[str]) -> List[List[str]]:

        result = []
        anagramDict = {}  # anagram, [list]

        # loop through all the word in the list
        for i, iword in enumerate(strs):
            # at each word, sort them
            sortedWord = "".join(sorted(iword))

            # IF sortedWord not already in dictionary
            if (anagramDict.get(sortedWord) == None):
                # then add it
                anagramDict[sortedWord] = [iword]

            # elise if dictionary
            else:
                # append the value
                anagramDict[sortedWord].append(iword)

        for k, v in anagramDict.items():
            result.append(v)

        return result

    # Below is optimal solution from LeetCode Solutions
    # Time Complexity: O(NKlog⁡K)O(NK \log K)O(NKlogK)
    # Space Complexity: O(NK)O(NK)O(NK)

    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

class SolutionTest(unittest.TestCase):
    def test01(self):
        testlist = [["ate","eat","tea"],["nat","tan"],["bat"]]
        result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        self.assertEqual(result, testlist, "")

if __name__ == '__main__':
    unittest.main()
