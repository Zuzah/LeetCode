'''
See Below for original Problem:
https://leetcode.com/problems/merge-two-sorted-lists/

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


Notes
- The input LinkedLists are pre-sorted. As such, numbers further along the list are greater
- Must utilize next pointer significantly: swaps either to l1 or l2 depending on which is lesser val
- Ininit an l3: ListNode. After end of loop, must set l3.val to lowestNumber, then assign next to ListNode(0)
- Init a lowestVal = 0. Assign value based on l1.val and l2.val comparison


Walkthrough
- use a while loop to iterate along l1 and l2, while suppliying l3 values either from l1 or l2 based on pointer valued
- Check if an l1 or l2 node is None. If so, simply set l3.next to the opposite node (i.e we don't comapre values, just assign)
    if (l1 is None):
        l3.next = l2
        break   #<--- we must break, not continue with checking values
- we compare l1.val and l2.val vie If else
    if l1.val < l2.val:
        smallest = l1.val
        l1.l2.next
    
    elif: l1.val > l2.va
        smallest = l2.val
        l2 = l2.next

- we then push the smallest as the new node to l3, and move along
    l3.val = smallest
    l3 = l3.next
 
'''
import unittest
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # vars
        head = l3 = ListNode(0) # head used to later return entire result l3 list
        smallestValue: int = 0 # used to track current smallest value between l1 and l2

        #while l1 or l2 has nodes/values
        while (l1 or l2):

            # handle if l1 or l2 are None
            if(l1 is None):
                l3.next = l2 # then focus onto l2 node
                break
            
            elif(l2 is None):
                l3.next = l1
                break

            if(l1 or l2):
                if (l1.val < l2.val):
                    # smallests
                    smallestValue = l1.val
                    l1 = l1.next
                
                elif (l2.val < l1.val):
                    smallestValue = l2.val
                    l2 = l2.next
            
                # assign l3 nodes
                print(smallestValue)
                l3.val = smallestValue
                if(l3):
                    l3 = ListNode(0)
                    l3.next

        return head
    
if __name__ == "__main__":
    myObj = Solution()
    digitXOne = ListNode(1)
    digitXTwo = ListNode(3)
    digitXThree = ListNode(5)
    digitXOne.next = digitXTwo
    digitXTwo.next = digitXThree
    digitXThree.next = None

    digitYOne = ListNode(2)
    digitYTwo = ListNode(4)
    digitYThree = ListNode(6)
    digitYOne.next = digitYTwo
    digitYTwo.next = digitYThree
    digitYThree.next = None
    myObj.mergeTwoLists(digitXOne, digitYOne)

            
            