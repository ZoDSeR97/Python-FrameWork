from app.models import base, user
from app.config.mySQLconnect import connectToMySQL

class Book(base.Base):
    db = "books"
    tbl_name = "books"
    def __init__(self, data) -> None:
        super().__init__(data)
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        
    @classmethod
    def get_one(cls, data, condition='id'):
        query = """
                SELECT * FROM books
                LEFT JOIN favorites ON books.id = books_id
                LEFT JOIN users ON users_id = users.id
                WHERE books.id=%(id)s
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        book.users = []
        for row in results:
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'], 
                'last_name': row['last_name'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at'],
            }
            book.users.append(user.User(user_data))
        return book
    
    @classmethod
    def get_all_notFav(cls, data):
        query = """
                SELECT * FROM books
                WHERE books.id NOT IN (SELECT books_id FROM books 
                LEFT JOIN favorites ON books.id = favorites.books_id
                WHERE users_id=%(id)s);
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