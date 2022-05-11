class addTwoNumbers():
    def addTwoNumbers(self, l1, l2):
        rev = ListNode(0)
        tail = rev
        counter = 0
        
        while l1 or l2 or counter:
            val1 = (l1.val if l1 else 0)
            val2 = (l2.val if l2 else 0)
            counter, result = divmod(val1 + val2 + counter, 10)
            
            tail.next = ListNode(result)
            tail = tail.next
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            
        return rev.next