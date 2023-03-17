from app import bcrypt
from app.models import base
from flask import flash
import re

class User(base.Base):
    db = 'account_db'
    tbl_name = 'users'
    def __init__(self, data) -> None:
        super().__init__(data)
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.mumbo_jumbo = data['mumbo_jumbo']
        
    @staticmethod
    def validate_registration(data):
        errors = {'reg':[]}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if len(data["first_name"]) < 2:
            errors["reg"].append("First Name should be at least 2 characters") # add our error message as a key value pair in our errors dictionary
        
        if len(data["last_name"]) < 2:
            errors["reg"].append("Last Name should be at least 2 characters")
        # test whether a field matches the pattern
        if len(data["email"]) < 5:
            errors["reg"].append("Email should be at least 5 characters")
        elif not EMAIL_REGEX.match(data['email']): 
            errors["reg"].append("Invalid email address!")
        # test whether email is unique
        elif User.get_one(data, condition='email'):
            errors["reg"].append("Email address already in use!")
            
        if not bool(re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$', data["password"])): # google this
            errors["reg"].append("Password must be at least 8 characters and contain at least 1 uppercase and 1 number!") 
        elif data["password"] != data['confirm']:
            errors["reg"].append("Password mismatch confirmation")
            
        for category, messages in errors.items(): # iterate over the keys and values of the dictionary
            for message in messages:
                flash(message, category) # flash all of our errors at once, while also assigning them category filters
        return not bool(errors['reg']) # will return true if no errors else will return false
    
    @staticmethod
    def validate_login(data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(data['email']): 
            errors["log"]="Invalid email or password"
        elif not errors:
            profile = User.get_one(data, condition='email')
            if not profile \
                and not bool(re.search(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$', data["password"]))\
                    and not bcrypt.check_password_hash(profile[0].password, data['password']+profile[0].mumbo_jumbo):
                    errors["log"]="Invalid email or password"
            
        for category, message in errors.items(): # iterate over the keys and values of the dictionary
            flash(message, category) # flash all of our errors at once, while also assigning them category filters
        return not bool(errors) # will return true if no errors else will return false