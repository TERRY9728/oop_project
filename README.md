# COMP 2090SEF OOP Project

## Task1: Library Management System - Simple Web App

This is a library management system based on Object-Oriented Programming and minimal full-stack development. Functions including books borrowing and returning, searching, and adding and deleting. 

### The main conception of OOP:
#### 1. Classes and Objects
- `User`: parent of Reader and Librarian.
- `Reader`: borrowing/returning books and retrieving reader infomation.
- `Book`: title and stock, as well as searching strategies.
- `Librarian`: adding/deleting books.

#### 2. Encapsulation
- Privite attribute and method: `__database_conn` and `__update()`.
- Public methods: `load_by_title()`, `reduce_stock()`, `login()`, etc..

#### 3. Inheritance
- `Reader` and `Librarian` inherit `User`.

#### 4. Polymorphism
- `Reader` and `Librarian`: the methods in two classes `is_exist()` and `login()` perform differently.

### Classes and Function
- Reader: Manage ID and name, borrow/return methods.
- Book: Manage book title, author and stock.
- LibraryManager: Provides operations and manages bookes.

---

### App Features
#### 1. Login: You can select your identity for doing related businesses. <br>
<img src="./images/homepage.png" alt="homepage" width="400"/>

#### 2. Searching a book by title
<img src="./images/readerpage.png" alt="readerpage" width="300"/>
<img src="./images/searching_demo.jpeg" alt="searching_demo" width="300"/>

#### 3. HTTP server handling
<img src="./images/httpserver_demo.png" alt="httpserver_demo" width="500"/>

#### 4. Sqlite3 connection
<img src="./images/database_record.png" alt="database_record" width="300"/>

---

### Getting Start
1. Clone the repository to local or directly download all the files.
2. Run the "main.py" file directly under **task1** directory.
3. You will get the loop-back address:
    ```
    >> python3 main.py
    http://127.0.0.1:8000
    ```
4. Open it in your browser. <br>
    <img src="./images/homepage.png" alt="homepage" width="500"/>

---

## Task2: Self-study on a Data Structure and Algorithm - Heap and Heapsort

### 1. Overview
    Heaps - tree-based data structures. 

    Heapsort - a comparison-based sorting algorithm using a heap.

Max-heap: every parent node is greater than or equal to its children;<br>
<img src="./images/max_heap.png" alt="max_heap" width="300"/>

Min-heap, every parent node is smaller than or equal to its children.<br>
<img src="./images/min_heap.png" alt="min_heap" width="300"/>

### 2. Data Structure: Heap
- ADT: A heap is a complete binary tree. In a max-heap, parent nodes are larger than children. Main operations: build heap, heapify, insert, extract root.
- Applications: Priority queues, task scheduling, Dijkstra's algorithm.

### 3. Algorithm: Heap Sort
- Idea: Build a max heap, then repeatedly swap the root (largest) with the last element, reduce heap size, and heapify the root. This sorts the array in place.
- Time Complexity: O(n log n) for all cases. Space: O(1).

### 4. Code Implementation
- `Heap` class: method includes `build_heap`, `heapify`, `heapsort`, `pop`, `extract_root` and `insert`.
- `max_heap` class: inherits `Heap` and implements `heapify` for max heap.
- `Min_Heap` class: inherits `Heap` and implements `heapify` for min-heap.