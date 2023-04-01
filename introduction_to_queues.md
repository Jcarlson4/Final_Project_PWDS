# Queues Tutorial.

Welcome to my Queues tutorial. Today we will be learning all about queues and there implementation when we are programing. I will discuss several different methods used for using queues and then present a problem for us to solve with a queue. 

## What is a Queue?

A queue in simple terms is like a line at a movie theater. Say you want to go and see the newest movie that just came out. You would arrive at the movie theater, enter into a line, and then proceed through the line until you arrived at the cash register to purchase your popcorn and movie tickets. This is a queue. A queue can take a certain amount of tasks and complete them in the order that they are recieved using threads on a computer. 

To do this, we will write some simple code to demonstrate how this can be done. 

## How to use a Queue?

You have found out what a queue is now is our opportunity to implement it using some simple code in python. 

In this tutorial, we will be talking about some different operations that will be useful when creating our queue. 

My wife is a teacher, she currently is teaching in a 1st grade classroom. Every morning when she arrives to work she takes roll call of her students. She takes roll call as the students come into the classroom. Once the student enters the classroom, we add them to our queue so that we know who arrived first and who arrived last. For our example code, we will show how she takes attendance using a queue. 

To prepare our environment, we will need to create an empty python list to be our queue. 

'''python
attendance_queue = []
'''

The first method that we are going to use with our queue is called "Enqueue". What this does, is allow us to add a name to our attendance sheet as they come into the queue. To do this, we will initialize our attendance queue by creating an empty list. Next, we will add to our queue or "Enqueue" using the .append mehtod. Afterwards, we will print the results.

'''python
attendance_queue = []

attendance_queue.append("Sally Adams")

print(attendance_queue)
'''

Congrats! You are well on your way to becoming a master with queues. Next, lets add another student. And lets say one of our students falls ill and leaves class right away. To remove something from our queue, we will use a "Dequeue" to remove it. 
There are a few ways to do this. If we want to remove, lets say, the last student who entered the class room. We would just use the .pop method to remove the last added thing into our queue. We could also use the pop method to remove from a different part of the list using the index method. If we wanted to remove a student from the beginning of the queue we could use pop method and indicate which item we want to remove from the queue. Here is an example with our classroom.

'''python
attendance_queue = []

attendance_queue.append("Sally Adams")
attendance_queue.append("Bucky Stan")
attendance_queue.append("Jeremiah Carlson")


print(attendance_queue)
'''

Here is our queue , it contains three students. Jeremiah has to leave class early so we will pop him from our queue.

'''python
attendance_queue.pop()
print(attendance_queue)
'''

Afterwards, Sally has to leave class early as well. To remove from a different part of our list, we will add an index value. Here we will add an index value of 0 to remove from the front of the list.

'''python
attendance_queue.pop(0)
print(attendance_queue)
'''

## A quick review.

As a summary, queues are used to help us organize data or tasks so that they will complete in a specific order. For our queues, they will finish in a "First come, First Serve" order. Some methods we talked about were, adding to our queue with the .append method and removing from our queue using the .pop method. These are called enqueue and dequeue respectively. 

## Your turn.

Say that you are working at a sit down restraunt here in Rexburg. You allow people to call ahead early to make reservations. Write a small program that creates a queue, adds ten people to it, then allows the person in the 5th spot of the queue cancel their reservations. Use the Enqueue and Dequeue methods to complete this task. 

Here is the solution when you are finished,

[1-solution_restraunt_queue](solution_restraunt_queue.md)