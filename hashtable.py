class HashTableSearch:
    def __init__(self):
        self.table = {}

    def insert(self, word, urls):
        self.table[word] = urls

    def search(self, word):
        return self.table.get(word, [])
