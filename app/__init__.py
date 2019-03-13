'''
This file is called by "from app import app" inside the app.py file. 

It includes all the imports to be used in the app (from allImports import *).
It also includes all the application files that are used as "pages" in the app
(e.g., "from app import start" imports all the code in start.py that is behind the start.html webpage)
'''

from allImports import *
from app import allImports

# Include an import for every python file that is serving a webpage
#import your new python files here. It is not a part of the module until it is imported
from app import start
from app import inventory
from app import addInventory
from app import editInventory
from app import addOrder
from app import addTunnels
from app import addTunnel
from app import deleteTunnel
from app import editTunnel
from app import editOrder
from app import deleteOrder
from app import order
from app import viewOrder
from app import addCustomer
from app import editCustomer
from app import customers
from auth import login_logout
from app import deleteCustomer
from app import designs
from auth import add_user