class Book:
    def __init__(self, book_id, title, author, stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.stock = stock

class InventoryManager:
    def __init__(self):
        self.books = {}
        self.order_queue = []

    def add_book(self, book_id, title, author, stock):
        book = Book(book_id, title, author, stock)
        self.books[book_id] = book

    def process_order(self, book_id, quantity):
        if book_id in self.books and self.books[book_id].stock >= quantity:
            self.books[book_id].stock -= quantity
            self.order_queue.append((book_id, quantity))
            return True
        else:
            return False

    def fulfill_orders(self):
        while self.order_queue:
            book_id, quantity = self.order_queue.pop(0)
            print(f"Fulfilled order for {quantity} copies of '{self.books[book_id].title}'")

def main():
    inventory_manager = InventoryManager()

    while True:
        print("\nOptions:")
        print("1. Add Book")
        print("2. Process Order")
        print("3. Fulfill Orders")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            book_id = int(input("Enter Book ID: "))
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            stock = int(input("Enter Stock Quantity: "))
            inventory_manager.add_book(book_id, title, author, stock)
            print("Book added to inventory.")

        elif choice == 2:
            book_id = int(input("Enter Book ID: "))
            quantity = int(input("Enter Order Quantity: "))
            if inventory_manager.process_order(book_id, quantity):
                print("Order processed successfully.")
            else:
                print("Insufficient stock or invalid book ID.")

        elif choice == 3:
            inventory_manager.fulfill_orders()

        elif choice == 4:
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
