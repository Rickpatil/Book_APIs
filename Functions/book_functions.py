from flask import app, request, jsonify
from flask_jwt_extended import create_access_token
import requests
from Database.DB import DB

class Book_data:
    def __init__(self):
        self.db = DB()

     # Generates jwt authentication token 
    def generate_access_token(self): 
        try:
            user_id = "user123"

            # Generate an access token
            access_token = create_access_token(identity=user_id)
            print(access_token)

            return {'access_token' : access_token}

        except Exception as e:
            return {'message' : str(e)}   

    # Creates a new record in db
    def create_book_record(self):
        try:
            data = request.get_json()
            # Input params
            book_name = data['book_name']
            book_description = data['book_description']
            total_pages = data['total_pages']
            author_name = data['author_name']
            publisher_name = data['publisher_name']

            cursor = self.db.cur()

            cursor.execute("""
                    INSERT INTO dbName.books (book_name, book_description, total_pages, author_name, publisher_name)
                    VALUES (%s, %s, %s, %s, %s)
                    """,
                    (book_name, book_description, total_pages, author_name, publisher_name)
            )
            
            self.db.conn.commit()
            self.db.conn.close()

            status_success = 'Success'
            message_success = 'A new book record created successfully'

            return {'Status' : status_success, 'Message' : message_success}

        except Exception as e:
            message_failure = str(e)
            status_failure = 'Failure'

            return{'Status' : status_failure,  'Message' : message_failure}

    # Fetches data from db
    def fetch_book_record(self):
        try:
            data = request.get_json()
            # Input params
            author_name = data['author_name']
            publisher_name = data['publisher_name']

            cursor = self.db.cur()

            cursor.execute("""
                    SELECT * FROM dbName.books 
                    WHERE author_name = %s or publisher_name = %s 
                """,
                (author_name, publisher_name))
    
            result = cursor.fetchall()
            return {'result' : result}
            

        except Exception as e:
            message =  str(e)
            return {'message' : message}

    # Deletes record from db
    def delete_book_record(self):
        try:
            data = request.get_json()
            # Input params
            book_id = data['book_id']

            cursor = self.db.cur()
            
            cursor.execute("""
                    DELETE FROM dbName.books 
                    WHERE book_id = %s
            """,
            (book_id,))

            self.db.conn.commit()
            self.db.conn.close()

            status_success = 'Success'
            message_success = 'Record deleted successfully'
            return {'status' : status_success, 'message' : message_success}

        except Exception as e:
            status_failure = 'Failure'
            message_failure = str(e)
            return {'status' : status_failure, 'message': message_failure}


########## Adding changes to changes-02 ################
### feature - 01 ####



