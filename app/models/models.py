from peewee import *
from secret import DB_PASSWORD, DB_USERNAME
import os

import datetime as dt
from datetime import datetime

# Create a database
from app.loadConfig import *
here = os.path.dirname(__file__)
cfg       = load_config(os.path.join(here, '../config.yaml'))
mainDB    = MySQLDatabase("tunnel_vision", 
                          host="localhost", 
                          user=DB_USERNAME, 
                          passwd=DB_PASSWORD)

# Creates the class that will be used by Peewee to store the database
class dbModel (Model):
  class Meta: 
    database = mainDB
    
"""
When adding new tables to the DB, add a new class here 
Also, you must add the table to the config.yaml file

Example of creating a Table

class tableName (dbModel):
  column1       = PrimaryKeyField()
  column2       = TextField()
  column3       = IntegerField()

For more information look at peewee documentation
"""
class User(dbModel):
  '''Table holding the users of the system'''
  uID      = PrimaryKeyField()
  username = CharField(unique=True)
  password = CharField()
  
  def is_active(self):
    """all users will be active"""
    return True
    
  def get_id(self):
    return str(self.uID)
    
  def is_authenticated(self):
    """ returns true if the user is authenticated"""
    return True
    
  def is_anonymous(self):
    return False
    
  def __repr__(self):
    return '{}'.format(self.username)
    
    

class Design(dbModel):
  '''table holding tunnel design information'''
  d_id = PrimaryKeyField()
  design_nm = TextField() #name of the design. Quonsic or Standard Gothic
  
  def __repr__(self):
    return "{}".format(self.design_nm)
  
class Inventory (dbModel):
  '''Table holding inventory information'''
  i_id           = PrimaryKeyField()
  description    = TextField()
  size           = IntegerField()
  cost           = IntegerField()
  size_unit      = TextField()
  cost_per       = TextField()
  quantity       = IntegerField()
  damaged        = IntegerField(default=0)
  
  def __repr__(self):
    return "{} {}{}".format(self.description, self.size, self.size_unit)
  
class Bow (dbModel):
  '''Table holding the types of bows and the inventory related'''
  b_id          = PrimaryKeyField()
  bow_type      = TextField()    #front, back, or middle
  design_name   = ForeignKeyField(Design, related_name="inventory_needed")
  inventory     = ForeignKeyField(Inventory)
  # this is the amount of inventory needed for the bow
  amountNeeded  = IntegerField(default=0)
  
 
class Customer (dbModel):
  '''Table holding customer information'''
  c_id          = PrimaryKeyField()
  first_name    = TextField()
  last_name     = TextField()
  email         = TextField()
  phone_number  = CharField()
  address       = TextField()

class Status(dbModel):
  s_id = PrimaryKeyField()
  status = CharField(unique = True)
  
class Order (dbModel):
  '''Table holding order information'''
  o_id          = PrimaryKeyField()
  status        = ForeignKeyField(Status, related_name="orders")
  #bow           = ForeignKeyField(Bow)    #bow_type will be through orderDesign table
  #number_of_bows= IntegerField()    #number of bows will be number of records in OrderDesign where order_id==this order_id
  price         = FloatField()    # price based on inventory
  created_date  = DateField(default=dt.datetime.now)
  notes         = TextField()
  customer      = ForeignKeyField(Customer, null=True) # to customer class
  cost          = IntegerField(null=True) # needs to be null so that it can be added later

class OrderDesign(dbModel):
  '''Many-to-many relationship between order and designs needed for order'''
  ord_design_id = PrimaryKeyField()
  order_id      = ForeignKeyField(Order,  related_name="tunnels")
  design_nm     = ForeignKeyField(Design)
  num_of_bows   = IntegerField()     #attribute for the number of bows in this tunnel
