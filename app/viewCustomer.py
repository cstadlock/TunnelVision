from allImports import * # goes on top
#decorator
@app.route("/customer/<c_id>" , methods = ["GET"])
def viewCustomer(c_id):
    """This function will get data from the database"""
    viewCustomer = Customer.get(Customer.c_id == c_id) 
    return render_template( "viewCustomer.html",
                            cfg = cfg, 
                            viewCustomer=viewCustomer)
    # return viewOrders.status.status