#Don't fear it is very easy

class Solution(object):
    def detectCycle(self, head):
        
        #Edge case:empty list or 1node
        if not head or not head.next:
            return None
        slow=head
        fast=head
        #phase 1: Find meeting point inside cycle
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                #cycle detected
                #phase 2: Find start of cycle
                slow=head#move slow to head
                #MOve both 1 step at a time
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next

                return slow#start of cycle

        return None
        