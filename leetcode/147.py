

"""
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

It repeats until no input elements remain.

The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains 
only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Example 1 :
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2: 
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def find_middle_ll(head) -> ListNode :
    slow, fast = head, head 
    prev = head
    while fast and fast.next: 
        prev = slow
        slow = slow.next 
        fast = fast.next.next

    # This is used to cut the remaining of the list
    if prev : 
        prev.next = None

    return slow

def merge_sort_ll(head)  :

    if not head or not head.next : 
        return head

    mid = find_middle_ll(head)
    lef_half = merge_sort_ll(head)
    right_half = merge_sort_ll(mid)
    
    return _merge_sub_ll(lef_half, right_half) 

def _merge_sub_ll(h1, h2) : 
    dummy = ListNode(-1)
    ans = dummy

    while h1 and h2: 
        if h1.val < h2.val : 
            ans.next = h1
            h1 = h1.next 
        else : 
            ans.next = h2 
            h2 = h2.next 
        ans = ans.next 
    ans.next = h1 if h1 else h2
    return dummy.next

class Solution:
    def insertionSortList(self, head) :
        head = merge_sort_ll(head)

        return head
    
    

if __name__ == "__main__": 
	head = ListNode(4,ListNode(2,ListNode(1,ListNode(3))))
	result = Solution().insertionSortList(head)
	while result: 
		print(result.val , end = '->')
		result = result.next
	print("None")