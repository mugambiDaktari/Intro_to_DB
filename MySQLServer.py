import mysql.connector

# Database connection details (replace with your own)
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Cliff4950*",
        database="alx_book_store"
    )
    print("Connection successful!")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    exit(1)
mycursor = mydb.cursor()

# Create a table named `customers` (if it doesn't exist)
mycursor.execute(
""" CREATE TABLE Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE
); 

CREATE TABLE Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);

CREATE TABLE Order_Details(
    orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT, 
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    book_id INT,
    FOREIGN KEY(book_id) REFERENCES Books(book_id),
    quantity DOUBLE
);"""
)


""" print("Table created successfully!") """

""" CREATE DATABASE IF NOT EXISTS alx_book_store;

USE alx_book_store;

CREATE TABLE Books(
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT,
    FOREIGN KEY(author_id) REFERENCES Authors(author_id),
    price DOUBLE,
    publication_date DATE
);

CREATE TABLE Authors(
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Customers(
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders(
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);

CREATE TABLE Order_Details(
    orderdetail_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT, 
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    book_id INT,
    FOREIGN KEY(book_id) REFERENCES Books(book_id),
    quantity DOUBLE
); """