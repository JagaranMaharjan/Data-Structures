# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 09:58:18 2020
"""
#Follows Last In First Out Principal (LIFO) 
class Stack(object):
    #created an empty array
    def __init__(self):
        self.item = []
    #push the element at the last index
    def push(self, items):
        self.item.append(items)
    #remove last item   
    def pop(self):
        self.item.pop()
        pass
    #fetch the first element of stack
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    #get total length of stack
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None
    #check stack is empty or not
    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False

if __name__ == "__main__":
    #created an object of Stack
    stack = Stack()
    #added two new elements on stack
    stack.push("1")
    stack.push("2")
    #display total len of stack
    print("The size of stack is :",stack.size())
    #fetch first element of stack
    print("First element of stack is :",stack.peek())    
    #remove last element from stack
    stack.pop()
    #display total len of stack
    print("The size of stack is :",stack.size())
    #fetch first element of stack
    print("First element of stack is :",stack.peek())    
    #check stack is empty or not
    print("Is stack empty ? \n", stack.isEmpty())