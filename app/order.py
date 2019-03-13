from allImports import * # goes on top
#decorator
@app.route("/orders" , methods = ["GET"])
@app.route("/", methods = ["GET"])
@login_required
def orders():
    """This function will get data from the database"""
    orders = Order.select()
    return render_template( "ordertables.html",
                            cfg = cfg, 
                            orders=orders
                          )