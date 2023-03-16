from app.models import base
from flask import flash

class Dojo(base.Base):
    db="dojo_survey"
    tbl_name="dojo"
    def __init__(self, data) -> None:
        super().__init__(data)
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        
    @classmethod
    def get_last(cls):
        query = """
            SELECT * FROM dojo
            ORDER BY id DESC LIMIT 1;
        """
        return super().get_result(query)
        
    @staticmethod
    def is_valid(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if 'location' not in data:
            flash("Select a location.")
            is_valid = False
        if 'language' not in data:
            flash("Select a language.")
            is_valid = False
        if len(data['comment']) < 3:
            flash("A feedback is needed.")
            is_valid = False
        return is_valid