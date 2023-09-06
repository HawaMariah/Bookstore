from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from bookstore import Books, Users, orders
from datetime import datetime

engine = create_engine('sqlite:///bookstore.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

def get_user_info():
    print("Welcome to Miss Mariah's Bookstore!")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email_address = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")

    # Create a new Users instance with the correct column names
    new_user = Users(
        first_name=first_name,
        last_name=last_name,
        email_address=email_address,  # Use the correct column name
        phone_number=phone_number
    )
    session.add(new_user)
    session.commit()


def search_books():
    while True:
        print("\nSearch for a book:")
        print("1. Search by Title")
        print("2. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title to search for: ")
            books = session.query(Books).filter(Books.title.like(f"%{title}%")).all()

            if not books:
                print("No matching books found.")
            else:
                for i, book in enumerate(books, start=1):
                    print(f"{i}. Title: {book.title}, Author: {book.author}, Price: ${book.price}, Quantity: {book.quantity}")

                try:
                    book_index = int(input("Enter the number of the book you want to buy (or '0' to go back): "))
                    if 1 <= book_index <= len(books):
                        selected_book = books[book_index - 1]
                        quantity = int(input(f"Enter the quantity to buy (1-{selected_book.quantity}): "))
                        if 1 <= quantity <= selected_book.quantity:
                            total_price = selected_book.price * quantity
                            print(f"Total cost: ${total_price}")
                            confirm = input("Confirm purchase (yes/no): ").strip().lower()
                            if confirm == "yes":
                                # Provide the current date and time as the order date
                                order_date = datetime.now()

                                new_order = orders(
                                    user_id=session.query(Users).order_by(Users.id.desc()).first().id,
                                    books_id=selected_book.id,
                                    quantity=quantity,
                                    order_date=order_date,  # Set the order date
                                    total_amount=total_price
                                )
                                session.add(new_order)
                                selected_book.quantity -= quantity
                                session.commit()
                                print(f"You have successfully purchased {quantity} copies of {selected_book.title}.")
                            else:
                                print("Purchase canceled.")
                        else:
                            print("Invalid quantity.")
                    elif book_index == 0:
                        break  # Break from the while loop
                    else:
                        print("Invalid book selection.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            break  # Break from the while loop
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    get_user_info()  # Get user information and add to the Users table
    search_books()   # Proceed with book search and purchase
