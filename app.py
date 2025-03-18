import json

# Global variable to store books
library = []

# Load books from the file
def load_library():
    global library
    try:
        with open("library.txt", "r") as file:
            library = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        library = []

# Save books to the file
def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)

# Add a new book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {"title": title, "author": author, "year": year, "genre": genre, "read": read_status}
    library.append(book)
    save_library()
    print("\n✅ Book added successfully!\n")

# Remove a book
def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            save_library()
            print("\n❌ Book removed successfully!\n")
            return
    print("\n⚠️ Book not found!\n")

# Search for a book
def search_book():
    choice = input("\nSearch by:\n1. Title\n2. Author\nEnter your choice: ")
    query = input("Enter the search term: ").strip().lower()

    results = [book for book in library if book["title"].lower() == query or book["author"].lower() == query]
    if results:
        print("\n🔎 Search Results:")
        for book in results:
            print(f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")
    else:
        print("\n⚠️ No matching books found!")

# Display all books
def display_books():
    if not library:
        print("\n📚 Your library is empty!\n")
        return
    print("\n📚 Your Library Collection:")
    for book in library:
        print(f"📖 {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {'✅ Read' if book['read'] else '❌ Unread'}")

# Display statistics
def display_statistics():
    total_books = len(library)
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print("\n📊 Library Statistics:")
    print(f"📚 Total books: {total_books}")
    print(f"📖 Books read: {read_books}")
    print(f"📊 Percentage read: {percentage_read:.2f}%")

# Main menu function
def main():
    load_library()
    
    print("\n" + "="*40)
    print("📚 Welcome to your Personal Library Manager! 📚")
    print("="*40)

    while True:
        print("\n" + "-"*40)
        print("1. 📖 Add a book")
        print("2. ❌ Remove a book")
        print("3. 🔍 Search for a book")
        print("4. 📚 Display all books")
        print("5. 📊 Display statistics")
        print("6. 🚪 Exit")
        print("-"*40)

        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("\n📁 Library saved to file. Goodbye! 👋")
            break
        else:
            print("\n⚠️ Invalid choice! Please enter a number between 1 and 6.")

# Run the program
if __name__ == "__main__":
    main()
