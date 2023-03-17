from app.config.mySQLconnect import connectToMySQL

class Base:
    db = ""
    tbl_name = ""
    def __init__(self, data) -> None:
        self.id = data['id']
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @staticmethod
    def contructArgs(data):
        return ", ".join(f"{key}=%({key})s" for key in data.keys() if key!="id")
    
    @classmethod
    def get_result(cls, query, data=None):
        results = connectToMySQL(cls.db).query_db(query, data)
        items = []
        if results:
            for item in results:
                items.append(cls(item))
        return items
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + cls.tbl_name + ";"
        return cls.get_result(query)
    
    @classmethod
    def get_one(cls, data, condition='id'):
        query = "SELECT * FROM "+cls.tbl_name+" WHERE "+f"{condition}=%({condition})s;"
        return cls.get_result(query, data)
    
    @classmethod
    def update(cls, data):
        query = cls.contructArgs(data)
        query = "UPDATE "+cls.tbl_name+" SET "+query+ " WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def save(cls, data):
        query = cls.contructArgs(data)
        query = "INSERT INTO "+cls.tbl_name+" SET "+query+";"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def remove(cls, data):
        query = "DELETE FROM "+cls.tbl_name+" WHERE id=%(id)s;"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db(query, data)
    