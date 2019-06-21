class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pointer = [None]*26
        self.end = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self
        for letter in word:
            if curr.pointer[ord(letter)-ord('a')] == None:
                curr.pointer[ord(letter)-ord('a')] = Trie()
            curr = curr.pointer[ord(letter)-ord('a')]
        curr.end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self
        for letter in word:
            num = ord(letter)-ord('a')
            if curr.pointer[num]:
                curr = curr.pointer[num]
            else:
                return False
        return curr.end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for letter in prefix:
            num = ord(letter)-ord('a')
            if curr.pointer[num]:
                curr = curr.pointer[num]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('a')
param_2 = obj.search('a')
param_3 = obj.startsWith('app')
obj.insert('apple')
param_4 = obj.search('app')
param_5 = obj.startsWith('app')
obj.insert('app')
param_6 = obj.search('app')
pass
