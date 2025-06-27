class Trienode:

    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False

class Solution:

    def __init__(self):
        self.root = Trienode()

    def insert(self, word):
        curr = self.root
        for i in word:
            index = ord(i) - ord("a")
            if not curr.children[index]:
                curr.children[index] = Trienode()
            curr = curr.children[index]
        curr.is_end_of_word = True

    def replaceWords(self, dictionary, sentence):
        """
        TC: (Nl + Ml)
        AS: (Nl + Ml)
        """

        for word in dictionary:
            self.insert(word)

        result = []
        for word in sentence.split():
            curr = self.root
            newStr = ""
            for i in word:
                index = ord(i) - ord("a")
                if not curr.children[index] or curr.is_end_of_word == True:
                    break
                else:
                    newStr += i
                    curr = curr.children[index]
            
            if curr.is_end_of_word:
                result.append(newStr)
            else:
                result.append(word)
            
        return " ".join(result)

            
