#you do not need a priority queue here, because you can only getMin()
#you cannot popMin(), if you need popMin() that we change the remainning list
#and we need a priority queue.
#This is problem is simple because you only need to the record the min value sofar

class MinStack(object):
    stack =[]
    min=[]

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min_sofar=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_sofar==[]:
            self.min_sofar.append(x)
        else:
            self.min_sofar.append(min(self.min_sofar[-1],x))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_sofar.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_sofar[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()