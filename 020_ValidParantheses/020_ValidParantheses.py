'''
See Below for original Problem:
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Input: "([)]"    <--- Note: It has correct correlating brackets BUT not correct positions
Output: false

Strategy
--------
- Use two data structures
    i. Dictionary where keys=CLOSED brackets, value= OPEN brackets.
      The CLOSED brackets must be keys in order to match top with dict[close] = open
        bracketDictionary = { ")": "("
                              "]": "["
                              "}": "{"}
    ii. Create a stack structure i.e 
        stack = []. Will append/pop paranthesis via LIFO policy

- Have exactly 1 for loop through lengh of str
- Inside the loop, have 2 IF conditions:
    - IF the s[i] in dictionary.values() i.e OPEN Brackets
        .: append
    - IF the s[i] in dictionary.keys() i.e CLOSED bracket
        .: set top = stack.pop() if stack else 'X' <--- we do this as stack might be empty.
        - Compare the top value against the bracketDictionary[s[i]]. If not equal, false

- Outside the loop, have an IF condition, return true is stack is empty, false if any content (i.e non-popped item)
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = [] # will store open brackets. Pop/Append peformed here
        validParanthesis =  {   ']': '[',
                                ')': '(' ,
                                '}': '{' 
                            }

        # iterate through length of string
        for i in range(0, len(s)):

            # check if str[i] is an open bracket
            if (s[i] in validParanthesis.values()):

                # append to the stack
                stack.append(s[i])

            # check if str[i] is an closed bracket
            if (s[i] in validParanthesis.keys()):
                # set popedvalue to later compare: stack COULD be empty when closed bracket is found
                top = stack.pop() if stack else '#'

                if (validParanthesis[s[i]] != top):
                    return False


        # if the stack has content
        if(stack):
            return False
        else:
            return True

if __name__ == "__main__":
    myObj = Solution()
    myObj.isValid("()[]{}{")
        
    