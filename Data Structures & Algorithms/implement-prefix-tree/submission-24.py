class TrieNode: 
    def __init__(self):
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        child = self.children
        for ch in word: 
            if ch in child: 
                child = child[ch].children
                continue
            child[ch] = TrieNode()
            child = child[ch].children
        child['end'] = True

    def search(self, word: str) -> bool:
        child = self.children
        for ch in word: 
            if ch in child:
                child = child[ch].children
            else:
                return False
        if 'end' in child: 
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        child = self.children
        for ch in prefix: 
            if ch in child: 
                child = child[ch].children
            else: 
                return False
        if child: 
            return True
        return False