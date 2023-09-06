from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bookstore import Books  # Import the Books class from your original file

# Define the database engine
engine = create_engine('sqlite:///bookstore.db', echo=False)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Define a function to add books
def add_books():
    books_data = [
        {"title": "The Enigmatic Echoes", "author": "Amelia Blackwood", "price": 1999, "quantity": 35},
        {"title": "Whispers in the Moonlight", "author": "Samuel Everhart", "price": 1495, "quantity": 42},
        {"title": "The Secret Garden of Serenity", "author": "Isabella Kensington", "price": 1299, "quantity": 28},
        {"title": "Chronicles of the Crimson Star", "author": "Vincent Thornfield", "price": 1750, "quantity": 20},
        {"title": "Eternal Embers", "author": "Penelope Sinclair", "price": 2199, "quantity": 50},
        {"title": "Lost in the Labyrinth", "author": "Oliver Northwood", "price": 1575, "quantity": 36},
        {"title": "The Midnight Mirage", "author": "Evangeline Sterling", "price": 1850, "quantity": 30},
        {"title": "Songs of the Siren", "author": "Lillian Rivers", "price": 1399, "quantity": 45},
        {"title": "Mysteries of the Whispering Woods", "author": "Benjamin Ashford", "price": 1625, "quantity": 25},
        {"title": "Echoes from Eternity", "author": "Aurora Nightshade", "price": 2075, "quantity": 22},
        {"title": "The Forgotten Chronicles", "author": "Nathaniel Evergreen", "price": 1450, "quantity": 38},
        {"title": "Whispers of the Silver Lake", "author": "Serena Monroe", "price": 1925, "quantity": 31},
        {"title": "The Phantom's Legacy", "author": "Gabriel Hawthorne", "price": 1199, "quantity": 40},
        {"title": "Lost Stars and Hidden Dreams", "author": "Isla Montgomery", "price": 1599, "quantity": 27},
        {"title": "The Enchanted Oasis", "author": "Rowan Blake", "price": 2250, "quantity": 18},
        {"title": "Tales from the Velvet Shadows", "author": "Lucinda Nightshade", "price": 1375, "quantity": 33},
        {"title": "The Chronicles of Azurea", "author": "Elijah Stone", "price": 1699, "quantity": 24},
        {"title": "Whispers of the Celestial Realm", "author": "Celeste Everhart", "price": 1425, "quantity": 29},
        {"title": "The Labyrinth of Dreams", "author": "Finnian Blackwood", "price": 1899, "quantity": 21},
        {"title": "Realm of the Mystic Moon", "author": "Seraphina Thornfield", "price": 2025, "quantity": 23}
    ]

    for book_info in books_data:
        book = Books(
            title=book_info["title"],
            author=book_info["author"],
            price=book_info["price"],
            quantity=book_info["quantity"]
        )
        session.add(book)

    session.commit()
    print("Books have been added to the database.")

if __name__ == "__main__":
    add_books()
