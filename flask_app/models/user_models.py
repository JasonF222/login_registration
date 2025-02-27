<<<<<<< HEAD
from os import stat
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
=======
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
>>>>>>> 6b4560508fd42a8eb1ee90c0e14a360711c04b61


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.pw_hash = data['pw_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
<<<<<<< HEAD
    
    
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());"
        return connectToMySQL('login_registration').query_db(query, data)

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('login_registration').query_db(query, data)
        user = []
        for one in results:
            user.append(cls(one))
        return user

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
=======
        
    @classmethod
    def save(cls, data):
        query = 'INSERT INTO users (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(pw_hash)s, NOW(), NOW());'
        return connectToMySQL('login_registration').query_db(query,data)
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL('login_registration').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, data):
        query = 'SELECT * FROM users WHERE email = %(email)s;'
>>>>>>> 6b4560508fd42a8eb1ee90c0e14a360711c04b61
        results = connectToMySQL('login_registration').query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

<<<<<<< HEAD
# User email Validation Static Method #

    @staticmethod
    def validate_email(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('INVALID EMAIL ADDRESS!')
            is_valid = False
        return is_valid

# User password Validation Static Method #

=======
    @staticmethod
    def validate_email( user ):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash('Invalid Email Address!')
            is_valid = False
        return is_valid
    
>>>>>>> 6b4560508fd42a8eb1ee90c0e14a360711c04b61
    @staticmethod
    def validate_pass( user ):
        if not len(user['pw1']) >= 8:
            flash('Password must be at least 8 characters!')
            return False
        if not user['pw1'] == user['pw']:
            flash('Passwords must match!')
            return False
        return True

<<<<<<< HEAD
# User name Validation Static Method #

=======
>>>>>>> 6b4560508fd42a8eb1ee90c0e14a360711c04b61
    @staticmethod
    def validate_names(user):
        if not len(user['first_name']) >= 3:
            flash('Name must be more than 3 characters.')
            return False
        if not len(user['last_name']) >= 3:
            flash('Name must be more than 3 characters.')
            return False
        if not user['first_name'].isalpha():
            flash('Names can only contain letters!')
            return False
        if not user['last_name'].isalpha():
            flash('Names can only contain letters!')
            return False
        return True