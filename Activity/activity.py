""""Goal: Analyze movie ticket sales using Python lists. ""
Role: You are a data analyst at a movie theater.
Audience: Your manager wants a summary report on ticket sales.
Situation: The theater records ticket sales in a list of tuples, where each tuple contains:
Movie Name (String)
Tickets Sold (Integer)
Ticket Price (Float, PHP)

movies 
 ("Avengers: Endgame", 150, 350.00), 
("The Dark Knight", 100, 300.00), 
("Inception", 120, 280.00), 
("Titanic", 180, 320.00),
 ("Frozen II", 140, 250.00), 
("Joker", 130, 275.00) 

Product/Performance Task:
1. Create an algorithm and Flowchart 
2. Write a Python program that:
Stores the movie ticket sales data in a list of tuples.
Implements these operations:
a) Displays the ticket sales report in a readable format.
b) Finds and displays the highest-grossing movie (Tickets Sold × Ticket Price).
c) Sorts the movies alphabetically and displays the sorted list.
d) Calculates and displays total revenue from all movies.
e) Allows the user to add a new movie’s ticket sales and displays the updated list."""


movies =[("Avengers: Endgame", 150, 350.00), 
("The Dark Knight", 100, 300.00), 
("Inception", 120, 280.00), 
("Titanic", 180, 320.00),
 ("Frozen II", 140, 250.00), 
("Joker", 130, 275.00 )]
#a
def display_format():
    print("\nOrder List:")
    for movieNames, sales, price in movies:
        print(f"{movieNames}: Sales = {sales}, Price/Unit = ₱{price:.2f}")
#b
def most_expensive_product():
    most_expensive = max(movies, key=lambda x: x[2])
    print(f"\nMost Expensive Product: {most_expensive[0]} at ₱{most_expensive[2]:.2f} per unit")

#c
def sort_orders():
    sorted_orders = sorted(movies, key=lambda x: x[0])
    print("\nSorted Movie names:")
    for movieNames, sales, price in sorted_orders:
        print(f"{movieNames}: Quantity = {sales}, Price/Unit = ₱{price:.2f}")
  

def total_revenue():
    revenue = sum(quantity * price for _, quantity, price in movies)
    print(f"\nTotal Revenue: ₱{revenue:.2f}")

def add_new_product():
    product_name = input("\nEnter the product name: ")
    quantity = int(input("Enter the quantity: "))
    price_per_unit = float(input("Enter the price per unit: "))
    orders.append((product_name, quantity, price_per_unit))
    print("\nUpdated Order List:")
    sort_orders()

def main():
    display_format()
    most_expensive_product()
    sort_orders()
    total_revenue()

main()