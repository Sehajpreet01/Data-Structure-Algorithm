class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
            self.length += 1

    


    
firstnode = LinkedList(11)
print(firstnode.head.value)


# secondnode = LinkedList(12)
# print(secondnode.head.value)

firstnode.append(13)
print(firstnode.tail.value)


















# def print_list(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.value)
    #         temp = temp.next

    # def append(self,value):
    #     new_node = Node(value)
    #     if self.head is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1
            

       
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.print_list()