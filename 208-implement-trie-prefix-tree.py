class Trie:

    def __init__(self):
        self.s = set()

    def insert(self, word: str) -> None:
        self.s.add(word)

    def search(self, word: str) -> bool:
        return word in self.s

    def startsWith(self, prefix: str) -> bool:
        return any(word.startswith(prefix) for word in self.s)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
