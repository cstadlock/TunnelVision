from ..models.models import User

def getUser(username):
    """ gets the a user based on a username 
        
        Args:
            username (str): the username of the username
            
        Returns:
            User Object: the user or none"
    """
    user = (User.select()
                .where (User.username == username))
                
    if user.exists():
        return user.get()
    else:
        return None