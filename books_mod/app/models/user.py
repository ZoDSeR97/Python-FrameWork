from app.models import base
from app.models import book
from app.config.mySQLconnect import connectToMySQL

class User(base.Base):
    db = "books"
    tbl_name = "users"
    def __init__(self, data) -> None:
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
    
    @classmethod
    def get_one(cls, data):
        query = """
                SELECT * FROM users 
                LEFT JOIN favorites ON users.id = favorites.users_id
                LEFT JOIN books ON favorites.books_id = books.id
                WHERE users.id=%(id)s 
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        user = cls(results[0]) # create an instance of this user
        user.favBooks = [] # List of this user favorites book
        for books in results:
            book_info = {
                'id': books['books.id'],
                'title': books['title'],
                'num_of_pages': books['num_of_pages'],
                'created_at': books['books.created_at'],
                'updated_at': books['books.updated_at']
            }
            user.favBooks.append(book.Book(book_info))
        return user
    
    @classmethod
    def get_all_notFav(cls, data):
        query = """
                SELECT * FROM users
                WHERE users.id NOT IN (SELECT users.id FROM users
                LEFT JOIN favorites ON users.id = users_id
                WHERE books_id=%(id)s);
                """
        results = connectToMySQL(cls.db).query_db(query, data)
        items = []
        if results:
            for item in results:
                items.append(cls(item))
        return items
    
    @classmethod
    def save_fav(cls, data):
        query = super().contructArgs(data)
        query = "INSERT INTO favorites SET " + query
        return connectToMySQL(cls.db).query_db(query, data)