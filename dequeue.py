# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 11:03:42 2020
"""
#Follows both FIFO and LIFO principal
class Deque(object):
    #initalize the deque
    def __init__(self):
        self.items = []
        
    def add_front(self, data):
        self.items.insert(0, data)
    
    def add_rear(self, data):
        self.items.append(data)

    def remove_front(self):
        if self.items == []:
            self.items.pop()
        return "Cannot remove. No items are there"
        
    def remove_rear(self):
        self.items.pop(0)
    
    #check deque is empty or not
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    #get total length of deque
    def size(self):
        if self.items:
            return len(self.items)
        else:
            return None
    
    def peek_front(self):
        return self.items[-1]
    
    def peek_rear(self):
        return self.items[0]

if __name__ == "__main__":
    #created an object of Deque
    deque = Deque()
    deque.add_front(1)
    deque.add_front(2)
    print("Size :", deque.size())
    deque.remove_rear()
    print("Size :", deque.size())