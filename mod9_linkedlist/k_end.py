"""
Write a function that, when given a Singly Linked List and an integer k, will return the kth element from the end of the list.

"""
### do not modify this class


class LinkedNode:
  def __init__(self, data):
    self.data = data
    self.next = None

### do not modify this class, or any of the methods in it, other than kth_from_the_end()
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
  def kth_from_the_end(self, k):
    # Method 1: using length
    # iterate over the LL
    # curr_node = self.head
    # node_position = 0
    # while curr_node.next != None:
    #   curr_node = curr_node.next
    #   node_position += 1
    # curr_node = self.head
    # for _ in range(node_position - k):
    #   curr_node = curr_node.next
    # return curr_node.data
    # >>>>>>>>>>>>>>>>>>>>
    # Method 2: using two pointers
    current_node = self.head
    k_step_ahead_node = self.head
    counter = 0
    # the following loop will move the pointer to kth node
    # NOTE: counter <= k starts counting from 0. counter < k starts counting from 1
    while k_step_ahead_node and counter <= k:
        k_step_ahead_node = k_step_ahead_node.next
        counter += 1
    # base case k is larger than linkedlist
    if not k_step_ahead_node:
        return f"{k} is greater than length of the LinkedList"
    # in this loop first pointer starts at the head and second pointer is on kth element
    # when second pointer equals to None, we reach the kth element from the end
    while current_node and k_step_ahead_node:
        current_node = current_node.next
        k_step_ahead_node = k_step_ahead_node.next
    return current_node.data


ll = LinkedList()
ll.extend(['A', 'B', 'C', 'D', 'E'])

print(ll.kth_from_the_end(3))
