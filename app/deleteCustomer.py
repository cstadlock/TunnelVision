from allImports import * #import everything
#decorator
@app.route("/deleteCustomer/<c_id>" , methods = ["GET","POST"])
@login_required
def deleteCustomer(c_id):
    """Deletes a customer and all the data associated with that customer"""
    page = request.path
    c_id = int(c_id)
    if request.method=="GET":
        return render_template("deleteCustomer.html",
                               cfg = cfg)
    data = request.form
    customer = Customer.get(Customer.c_id == c_id)  #get the customer
    customer.delete_instance()    #deletes customer and linked data
    return redirect(url_for("customers"))