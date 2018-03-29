class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.isword=False
        self.child={}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self
        for i,ch in enumerate(word):
            if ch not in node.child:
                node.child[ch]=WordDictionary()
            node= node.child[ch]
            
        node.isword=True
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.searchnode(self,word)
        
    def searchnode(self,cnode,word):
        node = cnode
        if word=="":
            return node.isword
        for i,ch in enumerate(word):
            if ch!='.':
                if ch not in node.child:
                    return False
                node=node.child[ch]
            else:
                for subnode in node.child:
                    if self.searchnode(node.child[subnode],word[i+1:]):
                        # print(word[i+1:],self.searchnode(subnode,word[i+1:]))
                        return True
                return False
        return node.isword
            
            
                    
                    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)