class Node:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = Node()

    def get(self, index: int) -> int:
        
        index += 1
        temp = self.head

        for _ in range(index):
            if temp == None:
                return -1
            temp = temp.next
        
        if temp == None:
            return -1
        
        return temp.val

        # temp = self.head
        # temp = temp.next
        # """ for i in range(index):
        # temp = temp.next
        # return temp.value"""
        # i = 0
        # while index != i:
        #     temp = temp.next
        #     i +=1
        # return temp.value

    def addAtHead(self, val: int) -> None:
       
        self.addAtIndex(0, val)

        # newNode = Node(val)
        # newNode.next = self.head.next
        # self.head.next = nextNode

    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp and temp.next:
            temp = temp.next

        temp.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:

        temp = self.head

        for _ in range(index):
            if temp == None:
                return
            temp = temp.next
        
        if temp == None:
            return

        newNode = Node(val)
        newNode.next = temp.next
        temp.next = newNode

        # curr = self.head.next
        # for i in range(index - 1):
        #     curr = curr.next
        # newNode = Node(val)
        # newNode.next = curr.next
        # curr.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head

        for _ in range(index):
            if temp == None:
                return
            temp = temp.next
        if temp == None:
            return
        if temp.next:
            temp.next = temp.next.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)