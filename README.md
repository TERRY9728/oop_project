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

