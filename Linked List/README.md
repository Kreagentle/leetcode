# Create Simple Singly Linked List DS

Write a code in the language of your choice to implement a singly linked list. A singly linked list has the following properties:
* Each node contains a piece of data. Node class constructor  takes a value as an argument and initializes the value attribute of the node.
* Each node also holds a reference (or link) to the next node in the list. A  next attribute, initialized to None, which will store a reference to the next node in the list.
* LinkedList class constructor takes a value as an argument and creates new node object based on Node class with that value.
head and tail attributes of the linked list to point to the new node.
* A length attribute, initialized to 1, which represents the current number of nodes in the list.

# Insertion at the Beginning of a Singly Linked List

Write a function to insert a new element at the beginning of a singly linked list. LinkedList and Node class are already provided.

# Insertion at the End of a Singly Linked List

Write a method to insert a new element at the end of a singly linked list. The logic should cover edge cases such as empty linked list or linked list with some elements in it.

# Deletion from a Singly Linked List

Write a function to delete a node from a singly linked list. The function should take the index(starting from 0) of the node to be deleted as a parameter.

# Reverse a Singly Linked List

Write a function to reverse a singly linked list. The function should return a new linked list that is the reverse of the original list.

```sh
Original singly linked list:   1 -> 2 -> 3 -> 4 -> 5
Reversed singly linked list:  5 -> 4 -> 3 -> 2 -> 1
```

# Middle of a Singly Linked List

Write a function to find and return the middle node of a singly linked list. If the list has an even number of nodes, return the second of the two middle nodes.

# Remove Duplicates from a Singly Linked List

Given a singly linked list, write a function that removes all the duplicates. use this linked list.

```sh
Original Linked List - "1 -> 2 -> 4-> 3 -> 4->2"
Result Linked List - "1 -> 2 -> 4 -> 3
```

# Merge Two Sorted Linked List

You are given the heads of two sorted linked lists list1 and list2. 
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

```sh
Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3: 
Input: list1 = [], list2 = [0]
Output: [0]
```

# Remove Duplicates

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 

```sh
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

# Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

```sh
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]
Example 2:
Input: head = [], val = 1
Output: []
Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
```

# Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
