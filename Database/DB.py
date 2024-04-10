import mysql.connector as sql

class DB:
    host = ''
    port = ''
    user = ''
    password = ''
    database = ''

    def __init__(self):
        self.conn = sql.connect(host = self.host, port = self.port, user = self.user, 
                                    password = self.password, database = self.database)
        
        self.create_books_table()

    def cur(self):
        return self.conn.cursor()

        
    def create_books_table(self):
        cursor = self.cur()
        query = '''
            CREATE TABLE IF NOT EXISTS dbName.books (
                book_id INT AUTO_INCREMENT,
                book_name VARCHAR(50),
                book_description VARCHAR(255),
                total_pages INT,
                author_name VARCHAR(50),
                publisher_name VARCHAR(50),
                PRIMARY KEY (book_id)
            );
        '''
        cursor.execute(query)
        self.conn.commit()