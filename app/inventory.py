from allImports import * # goes on top
#decorator
@app.route("/inventory" , methods = ["GET"])
@login_required
def inventory():
    """This function will get data from the database"""
    inventory = Inventory.select()
    return render_template( "inventory.html",
                            cfg = cfg, 
                            inventory=inventory
                          )
#Make sure to create the html inside of templates
#Make sure to place from app import page1 inside of __init__.py so that initilizer knows whats in the module

@app.route("/delete/inventory/<int:i_id>", methods=["GET", "POST"])
@login_required
def delete_inventory(i_id):
  """ deletes inventory """
  if request.method=="GET":
      return render_template("deleteOrder.html",
                             cfg = cfg)
  data = request.form
  inventory_item = Inventory.get(Inventory.i_id == i_id)  #get the order
  inventory_item.delete_instance(recursive = True, delete_nullable = True)    #deletes order and dependents
  return redirect(url_for("inventory"))

def reduceOrderInventory(order_id):
  """ reduces the inventory needed for an order """
  tunnels = OrderDesign.select().where(OrderDesign.order_id == order_id)
  for tunnel in tunnels:
    print tunnel.design_nm.d_id, tunnel.num_of_bows
    reduceDesignInventory(tunnel.design_nm.d_id, tunnel.num_of_bows)
    
def returnOrderInventory(order_id):
  """ returns the inventory for an order """
  tunnels = OrderDesign.select().where(OrderDesign.order_id == order_id)
  for tunnel in tunnels:
    returnDesignInventory(tunnel.design_nm.d_id, tunnel.num_of_bows) 

def reduceDesignInventory(designID, numberOfBows):
  """Reduces the inventory needed for a design
  :param designID - the id of the design that we are using
  :param numberOfBows - the length of the designID"""
  # reduce front bow inventory
  reduceBowInventory(designID, "front")
  # reduce back bow inventory
  reduceBowInventory(designID, "back")
  # reduce the middle bows
  reduceBowInventory(designID, "middle", numberOfBows)
  
def returnDesignInventory(designID, numberOfBows):
  """returns the inventory needed for a design 
    :param designID: the id of the design
    :param numberOfBows: the length of the design
  """
  # return front bow inventory
  returnBowInventory(designID, "front")
  # return back bow inventory
  returnBowInventory(designID, "back")
  # return the middle bows
  returnBowInventory(designID, "middle", numberOfBows)
  

def reduceBowInventory(designID, bowType, numberOfBows = 1):
  """this function reduces the inventory of one or several bows
     :param designID: the id of the design that needs to be reduced
     :param bowType: which bow type needs to be reduced (front, middle, back)
     :param numberOfBows: length of the design used with middle bows :default 1
  """
  mainDB.execute_sql(("UPDATE inventory"
                  " JOIN bow"
                  " ON bow.inventory_id = inventory.i_id"
                  " AND  `bow`.`design_name_id` = %s "
                  " AND bow.bow_type =  %s"
                  " SET quantity = quantity - (bow.amountNeeded * %s)"), 
                  (designID, bowType, numberOfBows))
                  
def returnBowInventory(designID, bowType, numberOfBows=1):
  """This function will return the inventory to the inventory table for one
     or several bows
     :param designID: the id of the design that needs to be returned
     :param bowType: which bow type needs to be returned (front, middle, back)
     :param numberOfBows: length of the design used with middle bows :default 1
  """
  
  mainDB.execute_sql(
                     ("UPDATE inventory"
                      " JOIN bow"
                      " ON bow.inventory_id = inventory.i_id"
                      " AND  `bow`.`design_name_id` = %s "
                      " AND bow.bow_type =  %s"
                      " SET quantity = quantity + (bow.amountNeeded * %s)"), 
                      (designID, bowType, numberOfBows)
                      )
     