


class ListNode: 
	def __init__(self, val, next = None) :
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


if __name__ == "__main__":
	temp = merge_sort_ll(ListNode(-1,ListNode(5,ListNode(3,ListNode(0,ListNode(4,ListNode(0)))))))
	while temp: 
		print(temp.val) 
		temp = temp.next