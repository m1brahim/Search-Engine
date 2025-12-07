class AVLNode:
    def __init__(self, word, urls):
        self.word = word
        self.urls = urls
        self.left = None
        self.right = None
        self.height = 1

class AVLSearch:
    def __init__(self):
        self.root = None

    def height(self, n):
        return n.height if n else 0

    def balance(self, n):
        return self.height(n.left) - self.height(n.right)

    def rotate_right(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, word, urls):
        self.root = self._insert(self.root, word, urls)

    def _insert(self, node, word, urls):
        if node is None:
            return AVLNode(word, urls)

        if word < node.word:
            node.left = self._insert(node.left, word, urls)
        elif word > node.word:
            node.right = self._insert(node.right, word, urls)
        else:
            node.urls = urls
            return node

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        if balance > 1 and word < node.left.word:
            return self.rotate_right(node)
        if balance < -1 and word > node.right.word:
            return self.rotate_left(node)
        if balance > 1 and word > node.left.word:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        if balance < -1 and word < node.right.word:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

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
