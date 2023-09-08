
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from bookstore import Books, Users, orders, exchange
from datetime import datetime


engine = create_engine('sqlite:///bookstore.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
def sort_books_by_price():
    print("\nSort books by Price:")
    books = session.query(Books).order_by(Books.price).all()

    if not books:
        print("No books found.")
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
                    action = input("Do you want to buy ? (y/n): ").strip().lower()

                    if action == "y":
                        confirm = input("Confirm purchase (yes/no): ").strip().lower()
                        if confirm == "yes":
                            order_date = datetime.now()
                            new_order = orders(
                                user_id=session.query(Users).order_by(Users.id.desc()).first().id,
                                books_id=selected_book.id,
                                quantity=quantity,
                                order_date=order_date,  
                                total_amount=total_price
                            )
                            session.add(new_order)
                            selected_book.quantity -= quantity
                            session.commit()
                            print(f"You have successfully purchased {quantity} copies of {selected_book.title}.")
                        else:
                            print("Purchase canceled.")
            elif book_index == 0:
                return
            else:
                print("Invalid book selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def exchange_books():
    print("\nExchange a book:")
    user_title = input("Enter the title of the book you want to exchange: ")

    matching_books = session.query(Books).filter(Books.title.like(f"%{user_title}%")).all()

    if not matching_books:
        print(f"No books found with the title '{user_title}'.")
        return

    print("\nMatching books:")
    for i, book in enumerate(matching_books, start=1):
        print(f"{i}. Title: {book.title}, Author: {book.author}")

    try:
        selected_book_index = int(input("Enter the number of the book you want to exchange with (or '0' to cancel): "))

        if 1 <= selected_book_index <= len(matching_books):
            selected_book = matching_books[selected_book_index - 1]

            user_book_title = input("Enter the title of the book you have: ")
            user_book_author = input("Enter the author of the book you have: ")
            fee = 100

            new_exchange = exchange(
                original_id=selected_book.id,
                order_date=datetime.now(),
                book_name= user_book_title
            )

            session.add(new_exchange)

            # Charge fee
            total_price = selected_book.price - fee

            new_order = orders(
                user_id=session.query(Users).order_by(Users.id.desc()).first().id,
                books_id=selected_book.id,
                quantity=1,  
                order_date=datetime.now(),
                total_amount=total_price
            )

            session.add(new_order)

            print(f"\nYou have successfully exchanged '{user_book_title}' by '{user_book_author}' for '{selected_book.title}' by '{selected_book.author}' for a fee of ${fee}.")
            session.commit()
        elif selected_book_index == 0:
            print("Exchange canceled.")
        else:
            print("Invalid book selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def get_user_info():
    print("Welcome to Miss Mariah's Bookstore!")
    
    user_info_provided = False

    while not user_info_provided:
        first_name = input("Enter your first name (or 'q' to quit): ")
        if first_name == 'q':
            return None
        last_name = input("Enter your last name: ")
        email_address = input("Enter your email address: ")
        phone_number = input("Enter your phone number: ")

        if not first_name or not last_name or not email_address or not phone_number:
            print("Please provide all required information.")
        else:
            new_user = Users(first_name=first_name, last_name=last_name, email_address=email_address, phone_number=phone_number)
            session.add(new_user)
            session.commit()
            user_info_provided = True

    return new_user

def search_books():
    while True:
        print("\nSearch for a book:")
        print("1. Search by Title")
        print("2. Sort by Price")
        print("3. Exchange Book")
        print("4. Quit")
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
                            action = input("Do you want to buy ? (y/n): ").strip().lower()

                            if action == "y":
                                confirm = input("Confirm purchase (yes/no): ").strip().lower()
                                if confirm == "yes":
                                    order_date = datetime.now()
                                    new_order = orders(
                                        user_id=session.query(Users).order_by(Users.id.desc()).first().id,
                                        books_id=selected_book.id,
                                        quantity=quantity,
                                        order_date=order_date,  
                                        total_amount=total_price
                                    )
                                    session.add(new_order)
                                    selected_book.quantity -= quantity
                                    session.commit()
                                    print(f"You have successfully purchased {quantity} copies of {selected_book.title}.")
                                else:
                                    print("Purchase canceled.")
                    elif book_index == 0:
                        break  
                    else:
                        print("Invalid book selection.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    
        elif choice == "2":
         sort_books_by_price()


        elif choice == "3":
            exchange_books()

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
   user = get_user_info()
   if user is not None:
        search_books()
   else:
        print("We're sorry to see you go.")




