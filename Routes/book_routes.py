from flask import Blueprint
from flasgger import swag_from
from flask_jwt_extended import jwt_required
from Functions.book_functions import Book_data


bookRoute = Blueprint('bookRoute', __name__, url_prefix='/bookroute')


# Generate jwt authentication token 
@bookRoute.route('generate_access_token', methods=['GET'])
@swag_from('book/generate_access_token.yml')
def generate_access_token():
    Book = Book_data()
    try:
        token = Book.generate_access_token()
        return token
    except:
        return 'Error'

# Creates a new record in db
@bookRoute.route('/create_book_record', methods=['POST'])
@jwt_required()
@swag_from('book/create_book_record.yml')
def create_book_data():
    Book = Book_data()
    try:
        create = Book.create_book_record()
        return create
    except:
        return "Error"

# Fetches data from db
@bookRoute.route('fetch_book_record', methods=['POST'])
@jwt_required()
@swag_from('book/fetch_book_record.yml')
def fetch_book_data():
    Book = Book_data()
    try:
        fetch = Book.fetch_book_record()
        return fetch
    except:
        return 'Error'

# Deletes record from db
@bookRoute.route('delete_book_record', methods=['POST'])
@jwt_required()
@swag_from('book/delete_book_record.yml')
def delete_book_data():
    Book = Book_data()
    try:
        delete = Book.delete_book_record()
        return delete
    except:
        return 'Error'
