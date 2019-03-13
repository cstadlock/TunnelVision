from allImports import * # import everything
from inventory import reduceOrderInventory, returnOrderInventory
#decorator
@app.route("/editOrder/<int:o_id>" , methods = ["GET", "POST"])
@login_required
def editOrder(o_id):
    page = request.path
    order = Order.get(Order.o_id == o_id)
    if request.method == "GET":
        #order = Order.select().where(Order.o_id == o_id)
        customers = Customer.select()
        statuses = Status.select()
        tunnels = OrderDesign.select().where(OrderDesign.order_id==o_id)  #all of the order's tunnels
        return render_template( "editOrder.html",
                            cfg = cfg, 
                            order=order,
                            customers = customers,
                            statuses = statuses, tunnels =tunnels)
    data = request.form    #returns dictionary of post data
    
    order.customer = data["customer"]
    order.price = data["Price"]
    old_status = order.status
    order.status = data["status"]
    
    updateStatus(old_status.status, order.status.status, order.o_id)
    
    order.notes = data["ordNotes"]

    order.save()
    return redirect(url_for("orders"))
    
def updateStatus(old_status, new_status, order_id):
    # do nothing is the status didn't change
    pending_delivery = "Pending Delivery" # when inventory  should be taken out
    if old_status == new_status:
        pass
    elif new_status == pending_delivery:
        reduceOrderInventory(order_id)
    elif old_status == pending_delivery:
        returnOrderInventory(order_id)