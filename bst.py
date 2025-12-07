class BSTNode:
    def __init__(self, word, urls):
        self.word = word
        self.urls = urls
        self.left = None
        self.right = None

class BSTSearch:
    def __init__(self):
        self.root = None

    def insert(self, word, urls):
        self.root = self._insert(self.root, word, urls)

    def _insert(self, node, word, urls):
        if node is None:
            return BSTNode(word, urls)
        if word < node.word:
            node.left = self._insert(node.left, word, urls)
        elif word > node.word:
            node.right = self._insert(node.right, word, urls)
        else:
            node.urls = urls
        return node

    def search(self, word):
        node = self._search(self.root, word)
        return node.urls if node else []

    def _search(self, node, word):
        if node is None:
            return None
        if node.word == word:
            return node
        if word < node.word:
            return self._search(node.left, word)
        return self._search(node.right, word)
