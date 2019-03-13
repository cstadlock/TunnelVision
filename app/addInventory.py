from allImports import * # goes on top
#decorator
@app.route("/addInventory" , methods = ["GET", "POST"])

def addNewInventory():
    
    page = request.path 
    if request.method == "GET":
        """This function will get data from the database"""
        addInventory = Inventory.select()
        return render_template("addInventory.html", cfg = cfg, addInventory=addInventory)
    
    data = request.form #returns dict of post data
    theNewInventory = Inventory.create (description = data["add_inventory_description"], size = int(data["add_inventory_Size"]), cost = int(data["add_inventory_cost"]), size_unit = data["add_inventory_size_unit"], cost_per = data["add_inventory_cost_per"], quantity = int(data["add_inventory_quantity"])) #This Saves All Of The Data You Insert.
    
    if theNewInventory.save(): # Redirect to Inventory Table To See The Newly Added Inventory
        return redirect(url_for("inventory"))

    return ""