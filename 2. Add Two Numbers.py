# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
import json
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        l3 = l4 = ListNode(0)
        while l1 or l2 or add:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            num = val1 + val2 + add
            add = 0
            if num // 10 > 0:
                add = 1
                num = num % 10
            l3.next = ListNode(num)
            l3 = l3.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return l4.next


def stringToListNode(input):
    # Generate list from the input
    numbers = [int(i) for i in input]

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


def main():
    str1 = str(input('input the first number:'))
    str2 = str(input('input the second number:'))
    l1 = stringToListNode(str1)
    l2 = stringToListNode(str2)

    ret = Solution().addTwoNumbers(l1, l2)

    out = listNodeToString(ret)
    print out


if __name__ == '__main__':
    main()
