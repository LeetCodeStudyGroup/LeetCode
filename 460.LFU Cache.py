class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache = {}
        self.lists = {}
        self.min_cnt = -1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.update(key)
            return self.cache[key].value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap == 0:
            return

        if key in self.cache:
            self.cache[key].value = value
            self.update(key)
        else:
            if self.cap == len(self.cache):
                node = self.lists[self.min_cnt].pop()
                if self.lists[self.min_cnt].head == None:
                    del self.lists[self.min_cnt]
                del self.cache[node.key]
            self.cache[key] = Node(key, value)
            self.min_cnt = 1
            if self.min_cnt not in self.lists:
                self.lists[self.min_cnt] = ListNode(self.min_cnt)
            self.lists[self.min_cnt].append(self.cache[key])
            self.cache[key].list = self.lists[self.min_cnt]

    def update(self, key):
        old = self.cache[key].list
        old.remove(self.cache[key])
        new_cnt = old.count + 1
        if new_cnt not in self.lists:
            self.lists[new_cnt] = ListNode(new_cnt)
        self.lists[new_cnt].append(self.cache[key])
        if old.head == None:
            del self.lists[old.count]
            if self.min_cnt == old.count:
                self.min_cnt += 1

class ListNode(object):
    def __init__(self, count):
        self.count = count
        self.head = None
        self.tail = None

    def append(self, node):
        node.list = self
        if self.tail:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        else:
            self.head = self.tail = node

    def pop(self):
        node = self.head
        self.head = self.head.next
        if self.head:
            self.head.pre = None
        else:
            self.tail = None
        return node

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.pre
        if node.pre:
            node.pre.next = node.next
        if node.next:
            node.next.pre = node.pre
        node.pre = node.next = None

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.pre = None
        self.list = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
