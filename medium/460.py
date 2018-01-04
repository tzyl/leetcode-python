from collections import defaultdict


class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.node_map = {}
        self.history = defaultdict(LinkedListWithTail)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.node_map[key]
        self.increment_frequency(node)
        return self.cache[key]


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if not self.capacity:
            return
        if key in self.cache:
            node = self.node_map[key]
            self.increment_frequency(node)
            self.cache[key] = value
        else:
            if self.size == self.capacity:
                lowest_frequency = min(self.history)
                lfu = self.history[lowest_frequency].tail
                self.history[lowest_frequency].delete(lfu)
                if self.history[lowest_frequency].empty():
                    del self.history[lowest_frequency]
                del self.cache[lfu.key]
                del self.node_map[lfu.key]
            node = Node(key)
            node.frequency = 1
            self.cache[key] = value
            self.node_map[key] = node
            self.history[node.frequency].insert(node)
            self.size = min(self.size + 1, self.capacity)

    def increment_frequency(self, node):
        self.history[node.frequency].delete(node)
        if self.history[node.frequency].empty():
            del self.history[node.frequency]
        node.frequency += 1
        self.history[node.frequency].insert(node)


class LinkedListWithTail(object):
    """Doubly linked list with insert to tail."""
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head is None

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if not self.empty():
            self.head.prev = x
        else:
            self.tail = x
        self.head = x
        x.prev = None

    def insert_tail(self, x):
        x.prev = self.tail
        if not self.empty():
            self.tail.next = x
        else:
            self.head = x
        self.tail = x
        x.next = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev
        else:
            self.tail = x.prev

    def traverse(self):
        print "KEY PREV NEXT"
        x = self.head
        while x is not None:
            print "%s\t%s\t%s" % (x.key,
                                  x.prev.key if x.prev is not None else None,
                                  x.next.key if x.next is not None else None)
            x = x.next


class Node(object):
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None
        self.frequency = 0

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.set(key,value)
