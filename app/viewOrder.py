from allImports import * # goes on top
#decorator
@app.route("/order/<o_id>" , methods = ["GET"])
@login_required
def viewOrder(o_id):
    """This function will get data from the database"""
    order = Order.get(Order.o_id == o_id) 
    return render_template( "viewOrder.html",
                            cfg = cfg, 
                            order=order)
    # return viewOrders.status.status
    