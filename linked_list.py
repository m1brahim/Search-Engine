class Node:
    def __init__(self, word, urls):
        self.word = word
        self.urls = urls
        self.next = None

class LinkedListSearch:
    def __init__(self):
        self.head = None

    def insert(self, word, urls):
        new_node = Node(word, urls)
        new_node.next = self.head
        self.head = new_node

    def search(self, word):
        curr = self.head
        while curr:
            if curr.word == word:
                return curr.urls
            curr = curr.next
        return []
