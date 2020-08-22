"""
Given a Tree class, create a method called add that accepts a Node, and inserts it into a tree such that the tree continues to be a Binary Search Tree. The method should return nothing.

A Binary Search Tree is a tree where every node has values greater than its data on the right-hand side, and values less than its data on the left-hand side, and all of the sub-tree nodes follow suit. Here's an example:
"""
import sys
sys.setrecursionlimit(1000)


class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None


class Tree:
  def __init__(self):
    self.root = None

  def print_bfs(self):
    if not self.root:
      return

    queue = [self.root]

    while len(queue) > 0:
      current_node = queue.pop(0)
      print(current_node.data)
      if current_node.left:
        queue.append(current_node.left)
      if current_node.right:
        queue.append(current_node.right)

  def in_order_traversal(self):
    nodes = []

    def dfs(node):
      if node:

        dfs(node.left)
        nodes.append(node.data)
        dfs(node.right)

    dfs(self.root)
    return nodes

  def add(self, node):
    if not self.root:
      self.root = node
      return

    def insert(root, node):

      if root.data > node.data:
        if root.left is None:
          root.left = node
        else:
          insert(root.left, node)
      else:

        if root.right is None:
          root.right = node
        else:
          insert(root.right, node)

    insert(self.root, node)
