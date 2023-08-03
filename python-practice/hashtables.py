#notes: provides data look up by key rather than by index
#behaves like a dictionary in python
#internally still uses a flat array
#static chaining , collisions are handled by creating a linked list where there are multiple matches 
#each index in the internal flat array is referred to as a "bucket"
#hash, insert, find and remove

from multiprocessing.sharedctypes import Value
from unittest import result


initial_capacity = 50

class Node:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.next = None
class HashTable:
    def __init__(self):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key,value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return None
        else:
            return node.value
    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.seize -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next
            return result
                











