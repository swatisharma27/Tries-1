class Trienode:

    def __init__(self):

        self.childen = [None]*26
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = Trienode()


    def insert(self, word):
        curr = self.root
        for i in word:
            index = ord[i] - ord['a']
            if not curr.childen[index]:
                curr.childen[index] = Trienode()
            curr = curr.childen[index] 
        curr.is_end_of_word = True

    def search(self, word):
        curr = self.root
        for i in word:
            index = ord(i) - ord("a")
            if not curr.childen[index]:
                return False
            curr = curr.childen[index]
        return curr.is_end_of_word
            
    def startswith(self, prefix):
        curr = self.root
        for i in prefix:
            index = ord(i) - ord("a")
            if not curr.childen[index]:
                return False
            curr = curr.childen[index]
        return True

