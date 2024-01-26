from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_basicauth import BasicAuth
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/bookstore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Flask-Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Basic Authentication
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'password'
basic_auth = BasicAuth(app)
# Define your database models (schema)
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(13), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'
    def serialize(self):
        """Serialize Book object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn,
            'price': self.price,
            'quantity': self.quantity
        }
# Create the database tables within the application context
with app.app_context():
    db.create_all()

# Adding a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(**data)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'}), 201

# Retrieving all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [book.serialize() for book in books]
    return jsonify(book_list)

# Retrieving a specific book by ISBN
@app.route('/books/<isbn>', methods=['GET'])
def get_book(isbn):
    book = Book.query.filter_by(isbn=str(isbn)).first()
    if book:
        return jsonify(book.serialize())
    return jsonify({'message': 'Book not found'}), 404

# Updating book details
@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.json
    book = Book.query.filter_by(isbn=str(isbn)).first()
    if book:
        book.title = data.get('title', book.title)
        book.author = data.get('author', book.author)
        book.price = data.get('price', book.price)
        book.quantity = data.get('quantity', book.quantity)
        db.session.commit()
        return jsonify({'message': 'Book updated successfully'})
    return jsonify({'message': 'Book not found'}), 404

# Deleting a book
@app.route('/books/<isbn>', methods=['DELETE'])
@basic_auth.required
def delete_book(isbn):
    book = Book.query.filter_by(isbn=str(isbn)).first()
    if book:
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted successfully'})
    return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
