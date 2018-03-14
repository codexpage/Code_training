class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic ={}
        self.keys=[]
        
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            self.dic[val].append(len(self.keys))
            self.keys.append((val,len(self.dic[val])-1))
            return False
    
        self.dic[val]=[len(self.keys)]
        self.keys.append((val,len(self.dic[val])-1)) #val and index in dic[val]


        return True        
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            return False
    
        # print(self.dic,val)
        index = self.dic[val][-1]
        last = self.keys[-1]
        out = self.keys[index]
        if index != len(self.keys)-1:
            self.dic[last[0]][last[1]] = index #update the new index for the last ele
            self.keys[index]= last #update last key to index key
           
        self.keys.pop()
        # print(index,self.keys)
        
        if len(self.dic[val]) == 1:
            self.dic.pop(val) #delete the entry
        else:
            del self.dic[val][out[1]]  #pop last index   
            #I am not sure the complex of del at specific index, could be O(n), if it is O(n), we can't use 'del', we can use
            #   a dict, remove from a dict is 100% O(1) or maybe a set()?
            # print("pop ",self.dic)
        return True
    

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.keys)[0]        
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
