"""A stack is a data structure that stores items in an Last-In/First-Out manner. This is frequently referred to as LIFO. 
This is in contrast to a queue, which stores items in a First-In/First-Out (FIFO) manner.
It’s probably easiest to understand a stack if you think of a use case you’re likely familiar with: the Undo feature in your editor.
"""
#Stack using Lists

myStack=[]
myStack.append("a")
myStack.append("b")
myStack.append("c")

print(myStack)

myStack.pop()  #Removes c
print(myStack)

myStack.pop()  #Removes b
print(myStack)

myStack.pop()  #Removes a
print(myStack)

# myStack.pop() #Throw an error (Pop from empty list)
# print(myStack)
"""Lists can run into speed issues as it grows The items in a list are stored with the goal of providing fast access to random elements in the list. At a high level, 
this means that the items are stored next to each other in memory. If your stack grows bigger than the block of memory that currently holds it,
then Python needs to do some memory allocations. This can lead to some .append() calls taking much longer than other ones."""


#Stacks using Deque (The collections module contains deque, which is useful for creating Python stacks. deque is pronounced “deck” and stands for “double-ended queue.”)

from collections import deque

      
# Declaring deque 
myStack1 = deque()
myStack1.append("a")
print(myStack1)

myStack1.append("b")
print(myStack1)

myStack1.append("c")
print(myStack1)


myStack1.pop()
print(myStack1)

myStack1.pop()
print(myStack1)

myStack1.pop()
print(myStack1)

"""The contiguous memory layout is the reason that list might need to take more time to .append()
some objects than others. If the block of contiguous memory is full, then it will need to get another
block, which can take much longer than a normal .append():

deque, on the other hand, is built upon a doubly linked list. In a linked list structure, each entry is stored in its own memory block and has a reference to the next entry in the list.

Getting myDeque[3] is slower than it was for a list, because Python needs to walk through each node of the list to get to the third element.

Fortunately, you rarely want to do random indexing or slicing on a stack. Most operations on a stack are either push or pop.

The constant time .append() and .pop() operations make deque an excellent choice for implementing a Python stack if your code doesn’t use threading."""

#Program to check for balanced parathesis
open_list = ["[","{","("]
close_list = ["]","}",")"]

def check(myString):
    stack = []
    for i in myString:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if(len(stack)==0):   #if the stack is empty, return unbalanced e.g (()))))
                return "Brackets are not balanced"
            else:
                stack.pop()
    if(len(stack)==0):
        print("Brackets are balanced")
    else:
        print("Brackets are not balanced")
string = "[[]]]"
print(check(string))
