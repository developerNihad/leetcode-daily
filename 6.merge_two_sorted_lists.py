class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 if list1 else list2
        
        return dummy.next

def create_linked_list(arr):
    head = ListNode()
    current = head
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return head.next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

test = Solution()
merged_list = test.mergeTwoLists(list1, list2)
print_linked_list(merged_list)