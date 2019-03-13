from allImports import * # goes on top
#decorator
@app.route("/editInventory/<i_id>" , methods = ["GET", "POST"])
@login_required
def editInventory(i_id):
    """This function will update data in the database"""
    page = request.path
    inventory = Inventory.get(Inventory.i_id == i_id)
    if request.method == "GET":
        #inventory = Inventory.get(Inventory.i_id == i_id)
        return render_template( "editInventory.html",
                                cfg = cfg, 
                                inventory=inventory)

    data = request.form
    
    inventory.cost = data["cost"]
    inventory.quantity = data["quantity"]
    inventory.damaged = data["damaged"]
    if inventory.save():
        return redirect(url_for("inventory"))