class TrieNode:
    def __init__(self):
        self.children = {}
        self.urls = None

class TrieSearch:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, urls):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.urls = urls

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return node.urls if node.urls else []
