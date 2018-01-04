class Solution(object):
    def lexicalOrder(self, n):
        lex_order = []
        current = 1
        for _ in xrange(n):
            lex_order.append(current)
            current = self.get_next(current, n)
        return lex_order

    def get_next(self, x, n):
        if 10 * x <= n:
            return 10 * x
        else:
            while (x % 10 == 9 or x >= n):
                x /= 10
            return x + 1


# Recursive solution too slow.
class Solution2(object):
    def lexicalOrder(self, n):
        lex_order = []
        for i in xrange(1, 10):
            self.lex_helper(lex_order, i, n)
        return lex_order

    def lex_helper(self, lex_order, i, n):
        if i > n:
            return
        lex_order.append(i)
        for d in xrange(10):
            self.lex_helper(lex_order, 10 * i + d, n)


# Too slow.
class TrieSolution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lex_order = []
        number_trie = NumberTrie()
        for i in xrange(1, n + 1):
            number_trie.insert(i)
        for num in number_trie.preorder_traversal():
            lex_order.append(num)
        return lex_order


class NumberTrie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        current = self.root
        for d in self.get_digits(num):
            if current.links[d] is None:
                current.links[d] = TrieNode()
            current = current.links[d]

    def get_digits(self, num):
        if num == 0:
            yield 0
            return
        x = num
        digit_count = 1
        while x / 10:
            digit_count += 1
            x /= 10
        for i in reversed(xrange(digit_count)):
            yield (num / 10 ** i) % 10

    def preorder_traversal(self):
        stack = []
        for d in reversed(xrange(10)):
            if self.root.links[d] is not None:
                stack.append((d, self.root.links[d]))
        while stack:
            num, node = stack.pop()
            yield num
            for d in reversed(xrange(10)):
                if node.links[d] is not None:
                    stack.append((num * 10 + d, node.links[d]))


class TrieNode(object):
    def __init__(self):
        self.links = [None] * 10


if __name__ == '__main__':
    # print Solution().lexicalOrder(100)
    # print TrieSolution().lexicalOrder(100)
    # print Solution().lexicalOrder(10458)
    Solution().lexicalOrder(5000000)
