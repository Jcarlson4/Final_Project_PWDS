# Sets Tutorial.

Welcome to my Sets tutorial. Today we will be learning all about sets and there implementation when we are programing. I will discuss several different methods used for using sets and then present a problem for us to solve with a queue. 

## What is a set?

In simple terms, a set is very similar to a list or a tuple. It helps us to store data easily and efficiently. Then why use a set? A set is useful for data that is contains a lot of duplicate values. It helps us to eliminate duplicates and to combine different sets looking for specific types of data that we need to pull for our application. For example; I used to work an on campus job where we would send out a newsletter to parents once a month. We would have a master list of parents and compare the new list of parents and remove the duplicates each month to find which parents were new so we didn't send multiple emails to the same parents. With a set, this can be used quickly and efficiently. 

To do this, we will write some simple code to demonstrate how this can be done. 

## How to use a Queue?

You have found out what a set is now is our opportunity to implement it using some simple code in python. 

In this tutorial, we will be talking about some different operations that will be useful when creating our set. 

We will be using the same example that I just presented talking about the set of parent emails used at Student Support. 


To start, we will need to create our set. 

' ' 'python
email_list = set()
' ' '
If we want to start the set with data already inserted, all we need to do is this, 

' ' ' python
email_list = set(["parent1@gmail.com", "parent2@hotmail.com", "parent3@yahoo.com"])
' ' ' 

To start, lets say that we want to add in some new emails to our set. To do this, we use the .add method. This allows us to insert an email into our set. However, our set does not care what order that it recieves or presents the information to us. This is an important note to make. 

' ' 'python
email_list = set()

email_list.add("parent4@gmail.com")

print(email_list)
' ' '

To remove an item from our set, all we need to do is use the .remove method. This allows us to remove a certain item from our set. If it is not there, it will give us an error instead. 

' ' 'python
email_list = set()

email_list.remove("parent4@gmail.com")

print(email_list)
' ' '

Sets are also an awesome way to check data between two collections of data. To do this, we have two main methods. An Intersection and a Union. The intersection takes the common data from our sets and the Union combines the two lists together removing our duplicates all together. 

To do this, we do the following. 

' ' 'python
example_set1 = set([1,2,3,4,5,6])
example_set2 = set([7,8,9,10,1,2])

example_intersection = example_set1.intersection(example_set2)

print(example_intersection)
' ' '

' ' 'python
example_set1 = set([1,2,3,4,5,6])
example_set2 = set([7,8,9,10,1,2])

example_union = example_set1.union(example_set2)

print(example_union)
' ' '

## A quick review.

As a quick review, sets are like lists and tuples where they help us store data. However, a set allows us to remove duplicates and to hold a colleciton of data that does not have redundancy within it. We have different methods to add, remove and compare two sets together. 

## Your turn.

I would like for you to create a program that takes an email list, then checks it against a master list for any duplicates and removes them. I want you to create the list by adding 4 emails to our master list and 3 emails to our new list. Then, you will need to compare the lists to find all the duplicates and remove them to create a new master list. 

Here is the solution when you are finished,

[1-solution_restraunt_queue](solution_restraunt_queue.md)