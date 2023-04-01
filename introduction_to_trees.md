# Trees Tutorial.

Welcome to my Trees tutorial. Today we will be learning all about Trees and there implementation when we are programing. I will discuss several different methods used for using trees and then present a problem for us to solve with a tree. 

## What is a Tree?
A tree when it boils down, is a likned list. It helps us to organize a set of numbers in a specific way. The reason why it is called a tree because it represents a tree structure. Starting with a root or starting number, then folding down into "leaves" which represent an organization of numbers in a Tree format. 

We'll demonstrate exactly how this works below. 

## How to use a Tree?

To use a tree, we need to follow a simple algorithm. Lets say we have a tree with a base root of 10 and we want to insert the number 15. What we'll do is compare 15 to ten. If the new number is larger than the original number , you will place it on the right side of the tree. If it is smaller, you will place it on the left. You will do this all the way until the number is the largest on the right OR is placed on the left and is the smaller number. Here is an image from my textbook for visual representation. 

![Textbook Tree Diagram](binary_tree.jpeg)

To initialize our tree, we will need to create a class and inatialize our tree. 

'''python
class Node:
    def __init__(self, data)
    self.left = None
    self.right = None
    self.data = data
'''

Once our tree is initialized, we will then need to compare our values to our root value through insertion. 

'''python
def insert(self, data):
    if self.data:
        if data < self.data:
        if self.left is None:
            self.left = Node(data)
        else:
            self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data
'''

We will then set up a method for printing our tree. 

'''python
def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print( self.data),
    if self.right:
        self.right.PrintTree()
'''

Next, to insert numbers into our tree, we will use the Insertion method. We will initialize our root to be a random number. Then we will insert some numbers. 

'''python
import random

root_number = random.randint(1,10)

root = Node(root_number)
root.insert(6)
root.insert(14)
root.insert(3)
root.PrintTree()
'''

## A quick review.
And there it is! That is how you create a tree and then analize it. To review, a tree is a way to organize data. We will always have a root number and from there we can start doing our sorting. If the new number is larger than the original, it goes to the right. It will then compare with any numbers there. If the second row number is larger, our number goes to the left of it. If it is larger, it moves to the right and continues down. 

## Your turn.

You will now create your own Tree! You will use the basis that we just created. However, we want to create a tree that is randomly generated. Make your insertions RANDOM so that we get a new tree each time that we run our program. Create your atleast 3 insertions.

[1-solution_restraunt_queue](solution_random_tree.md)