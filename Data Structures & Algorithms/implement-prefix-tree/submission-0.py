class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.endOfWord = False
        

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)

            node = node.children[char]

        node.endOfWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return node.endOfWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        
        return True
        
        