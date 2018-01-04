class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = get_number_from_linked_list(l1)
        y = get_number_from_linked_list(l2)
        return create_linked_list_from_number(x + y)


def get_number_from_linked_list(linked_list):
    x = 0
    i = 0
    current = linked_list
    while current is not None:
        x += current.val * 10 ** i
        i += 1
        current = current.next
    return x


def create_linked_list_from_number(x):
    current = ListNode(x % 10)
    if x / 10:
        current.next = create_linked_list_from_number(x / 10)
    return current


if __name__ == '__main__':
    # Definition for singly-linked list.
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None

    l1 = create_linked_list_from_number(243)
    l2 = create_linked_list_from_number(564)
    print get_number_from_linked_list(Solution().addTwoNumbers(l1, l2))
