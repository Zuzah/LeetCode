'''
See Below for original Problem:
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Strategy
- Since an int is not iterable, change input x ito an str i.e -321 to '-1', '3', '2', '1'.
- create an empty array. Then utlize list comprehension set it with stringified values of the int
        i.e myList = [i for i in str(x)]
- Create a negative sign flag with true/false if int x is negative. Use if/else to then strip the -1 value before evaluation
    i.e cannot iterate over '-', '1', '2' .: remove -
- create a bufferArray to house array after it is reversed
- iterate through the myList, perform reverse via myBuffer += myList[len(myList)-i-1]
- at end, convert the str back into an int. Apply by -1 if negative flag is true
'''

class Solution:
    def reverse(self, x: int) -> int:
        
        tempBuffer: str = ''
        returnValue:int = 0
        negativeFlag: bool = False
        intList: List = [] # use to house list comprehension results

        # check if input is a negative number (O(1))
        if (x < 0):
            negativeFlag = True
            # strip the '-1' via multiplications
            x = x*-1

        intList = [i for i in str(x)] # convert input to str

        # reverse the intList
        for i in range(0, len(intList)):
            # swap index: 1 to len, 2nd t len-2 etc
            tempBuffer+=intList[len(intList)-i-1]
        
        # convert buffer to an int
        returnValue = int(tempBuffer) * -1 if negativeFlag else int(tempBuffer)
        print(returnValue)
        
        return  returnValue

if __name__ == "__main__":
    myObj = Solution()
    myObj.reverse(-231)