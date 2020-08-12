"""
Write a method for a Linked List that returns the length of the linked list.

For example:

ll = LinkedList()
ll.extend([1, 2, 3, 4, 5])

ll.length() # returns 5
"""

### do not modify this class


class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than length()
### you may insert new methods if you like


class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def empty(self):
    return self.head == None

  def append(self, data):
    if self.empty():
      self.head = LinkedNode(data)
      self.tail = self.head
    else:
      new_node = LinkedNode(data)
      self.tail.next = new_node
      self.tail = new_node

  def extend(self, array):
    for element in array:
      self.append(element)

  # implement this method
  # return the length of the linked list, an integer value
  def length(self):
    ll_len = 1
    curr_node = self.head
    if self.empty():
      return 0
    while curr_node.next != None:
      curr_node = curr_node.next
      ll_len += 1
    return ll_len
