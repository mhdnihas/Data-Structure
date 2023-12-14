class MyLinkedList(object):

    def __init__(self, val=0):

        self.val = val
        self.next = None
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        current = self.head
        count = 0
        if index == count:
            return current.val

        while count != index and current:
            current = current.next
            count += 1
        if not current:
            print("hai")
            return -1
        if count == index and current:
            return current.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = MyLinkedList(val)
        new_node.next = self.head
        self.head = new_node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = MyLinkedList(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        count = 0
        new_node = MyLinkedList(val)
        current = self.head
        if index == count:
            self.head = new_node
            return
        prev = None
        while current:  # 1     3

            if index == count:
                new_node.next = current
                if prev:
                    prev.next = new_node
                else:
                    self.head = new_node
                return
            prev = current
            current = current.next
            count += 1

        if count == index:
            prev.next = new_node
        return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        count = 0
        current = self.head
        prev = None
        while count != index and current.next:
            prev = current
            current = current.next
            count += 1
        if count == index:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
obj=MyLinkedList()
obj.addAtHead(2)
obj.addAtIndex(0,1)
print(obj.get(1))