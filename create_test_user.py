""" DO NOT USE IN PRODUCTION!!!! """

from app.models.models import *
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password):
    """ creates a user """
    User(username=username, password=generate_password_hash(password)).save()
    
def check_credentials(username, password):
    """ checks the password hash. Assumes username exists"""
    user = User.get(User.username == username)
    return check_password_hash(user.password, password)
    
    
def main():
    
    USERNAME = "test_user"
    PASSWORD = "password"
    
    create_user(USERNAME, PASSWORD)
    
    assert(check_credentials(USERNAME, PASSWORD))
    
if __name__ == "__main__":
    main()
    