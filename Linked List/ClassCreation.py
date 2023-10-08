class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = self.head
        self.length = 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            temp = self.head
            for _ in range(self.length - 1):
                temp = temp.next
            temp.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            deleted_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            deleted_node.next = None
            self.length -= 1
            return deleted_node

        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next

            deleted_node = temp.next
            if deleted_node.next is None:
                self.tail = temp

            temp.next = temp.next.next
            deleted_node.next = None
            self.length -= 1
            return deleted_node

    def reverse(self):
        prev_node = None
        node = self.head
        while node is not None:
            new_node = node.next
            node.next = prev_node
            prev_node = node
            node = new_node
        self.head, self.tail = self.tail, self.head



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
