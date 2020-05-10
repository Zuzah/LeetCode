# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
Keep note of the structure of l1 and l2 with respect to numbers

i.e 342 = [2] -> [4] -> [3]
    465 = [5] -> [6] -> [4]
    ----- -----------------
    807 = [7] ->[0] -> [8]

'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        # vars
        carry: int = 0
        digit: int = 0
        l3: ListNode = ListNode(0)
        head = l3 # set aside head value to later return. Will display entire result lined list after processing

        # while values still in the lists or the carry
        while (l1 or l2 or carry):

            # if l1 has digit value
            if (l1):
                carry = carry + l1.val if l1 else carry + 0
                l1 = l1.next # shift l1

            # if l2 has digit value
            if(l2):
                carry = carry + l2.val if l2 else carry + 0
                l2 = l2.next
            
            digit = carry % 10 # provides us the right-most digit of the l1+l2 result. Will be placed in l3 node
            carry = carry // 10 # provides us the left-most digit of the l1++l2 result. Will be utilized in next loop

            # set the l3 node's value property
            l3.val = digit

            # if there are stil l1 or l2 or carry digits to be added
            if (l1 or l2 or carry):
                # then attach an empty node to the l3 result list; then shift index
                l3.next = ListNode(0)
                l3 = l3.next

        #print("Test the Values")
        #while(head):
        #    print(head.val)
        #    head = head.next

        return head

if __name__ == "__main__":
    myObj = Solution()
    digitXOne = ListNode(3)
    digitXTwo = ListNode(4)
    digitXThree = ListNode(2)
    digitXOne.next = digitXTwo
    digitXTwo.next = digitXThree

    digitYOne = ListNode(5)
    digitYTwo = ListNode(6)
    digitYThree = ListNode(4)
    digitYOne.next = digitYTwo
    digitYTwo.next = digitYThree
    

    myObj.addTwoNumbers(digitXOne, digitYOne)