# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # A linked list is a data structure where each item (node) stores data and a link to the next item.
        # has DATA and NEXT
        # U create  a node with  node1= Node(_)
        # then u CONNECt it .  node1.next=node2

        prev = None 
        #prev starts as none. this is what we want the old head's next to become


        curr = head
        #curr starts as the head. node 1


        while curr:  #basically while curr has a value itll continue to run. By the end it should have a value of none
            nxt = curr.next #this line saves the next link before the link gets overwritten


            curr.next = prev #flips the current node's arrow backwards

            prev = curr #moves the prev vallue up to the current node.
            curr = nxt #curr moves to the next node using the saved copy
            #eventually the "next" node will = None. Think what is last node in a reg linked list?
        return prev    
        #now prev , the old tail, is now the new head
        