class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                current.links[c] = TrieNode()
            current = current.links[c]
        current.isWord = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.links:
                return False
            current = current.links[c]
        return current.isWord

    def startsWith(self, prefix):
        current = self.root
        for c in prefix:
            if c not in current.links:
                return False
            current = current.links[c]
        return True


class TrieNode(object):
    def __init__(self):
        self.links = {}
        self.isWord = False
