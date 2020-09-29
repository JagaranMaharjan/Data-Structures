# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 10:38:45 2020
"""
#Follows First In First Out (FIFO) principal
class Queue(object):
    #initialize empty queue
    def __init__(self):
        self.items = []
    #check queue is empty or not
    def isEmpty(self):
        return self.items == []
    #add new elements to queue
    def enqueue(self, item):
        self.items.insert(0, item)
    #remove last element of queue
    def dequeue(self):
        self.items.pop()
        pass
    #get total length of queue
    def size(self):
        return len(self.items)
    #display queue value
    def printQueue(self):
        for item in self.items:
            print (item)

if __name__ == "__main__":            
    #created new object of queue            
    queue = Queue()
    #is queue is empty ?
    print("Check queue is empty or not :",queue.isEmpty())
    
    #add items in queue
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    
    #get len of queue
    print("The size of queue is :",queue.size())
    
    #display all value of queue
    print(queue.printQueue())
    
    #remove last element of queue
    print(queue.dequeue())
    
    #display all value of queue
    print(queue.printQueue())