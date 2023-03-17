from app.models import base
from flask import flash
import re

class Email(base.Base):
    db='email_db'
    tbl_name = 'emails'
    def __init__(self, data) -> None:
        super().__init__(data)
        self.name = data['name']
        
    @classmethod
    def get_last(cls):
        query = "SELECT * FROM emails ORDER BY id DESC LIMIT 1;"
        return super().get_result(query)[0]
    
    @staticmethod
    def is_valid(data):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['name']): 
            flash("Invalid email address!")
            is_valid = False
        if Email.get_one(data, condition='name'):
            flash("Email address already in use!")
            is_valid = False
        return is_valid