class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            self.remove(self.cache[key])
            self.append(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if self.capacity == 0:
            return

        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            if len(self.cache) == self.capacity:
                node = self.pop()
                del self.cache[node.key]
            self.cache[key] = Node(key, value)
        self.append(self.cache[key])

    def append(self, node):
        if self.tail:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def pop(self):
        node = self.head
        if self.head:
            self.head = self.head.next
            if self.head:
                self.head.pre = None
            else:
                self.tail = None
        return node

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if self.tail == node:
            self.tail = node.pre
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        node.pre = node.next = None

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None
