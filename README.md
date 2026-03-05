# Library Management System
## Project Introduction
This project is a library management system created based on Object-Oriented Programming **(OOP)**, Its functions include borrowing and returning books, searching books and writers and managing books. 
This project uses main OOP concepts: **Class and Objects, Encapsulation, Inheritance, and Polymorphism**.
## The main conception of OOP
### 1. Class and Objects ###
- Reader class: Manages infomation of reader and borrowing/returning books.
- Book class: Manages different book names and the situation of stock.
- SearchStrategy class: The base of searchstrategy.
- SearchByTitle / SearchByAuthor class: How to search.
- LibraryManager class: System management.
### 2. Encapsulation ###
- Use the privite attributes: such as _id_num, _borrowed_books, _stock, it can protect the inner data.
- During the public method: such as get_title(), reduce_stock(), it can access and edit data to ensure the security.
### 3. Inheritance ###
- SearchByTitle / SearchByAuthor class inherit SearchStrategy class.
### 4. Polymorphism ###
- The search method implement Polymorphism. Search_books which in the LibraryManager accepts different objects from SearchStrategy class and excutes different search logic.
## Class and Function ##
- Reader: Manage ID and name, Borrow and return methods.
- Book: Manage book name, author and stock.
- SearchStrategy: Defines search interface.
- SearchByTitle: It implement searching books during name.
- SearchByAuthor: It implement searching books during author.
- LibraryManager: Provides operations and manages bookes and readers.
## Project feature ##
- It can show the daily manage of library simply.
- It show the main and core princicples of OOP

---
# Task 2: Self-study on a New Data Structure and Algorithm - Heap and Heap Sort
## 1. Overview
We chose **Binary Heap** (data structure) and **Heap Sort** (algorithm) because they are not covered in the course. We implemented a max heap and will implement heap sort later.

## 2. Data Structure: Binary Heap
- **ADT**: A binary heap is a complete binary tree. In a max heap, parent nodes are larger than children. Main operations: build heap, heapify, get root, insert, extract root.
- **Applications**: Priority queues, task scheduling, Dijkstra's algorithm.

## 3. Algorithm: Heap Sort
- **Idea**: Build a max heap, then repeatedly swap the root (largest) with the last element, reduce heap size, and heapify the root. This sorts the array in place.
- **Time Complexity**: O(n log n) for all cases. Space: O(1).

## 4. Code Implementation
### File: `heap.py`
- `Heap` class: base class with `__init__`, `build_heap`, `heapify` (placeholder), and helper methods.
- `Max_Heap` class: inherits `Heap` and implements `heapify` for max heap.
- `Min_Heap` not yet implemented.

### How to Run
```python
from heap import Max_Heap
data = [1, 4, 3, 7, 8, 3, 6, 2, 7, 10]
maxheap = Max_Heap(data)
print(maxheap.data)  # Example output: [10, 8, 6, 7, 4, 3, 3, 2, 7, 1]

##Preliminary Results

##Future Work
##References
