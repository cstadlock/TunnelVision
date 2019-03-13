from allImports import * #import everything
#decorator
@app.route("/deleteOrder/<o_id>" , methods = ["GET","POST"])
@login_required
def deleteOrder(o_id):
    """Deletes an order and all the tunnels associated with that order"""
    page = request.path
    o_id = int(o_id)
    if request.method=="GET":
        return render_template("deleteOrder.html",
                               cfg = cfg)
    data = request.form
    order = Order.get(Order.o_id == o_id)  #get the order
    order.delete_instance(recursive = True, delete_nullable = True)    #deletes order and dependents
    return redirect(url_for("orders"))
    
    