from allImports import * # goes on top
#decorator
@app.route("/customers" , methods = ["GET", "POST"])
@login_required
def customers():
    """This function will get data from the database"""
    page = request.path 
    customers = Customer.select()
    return render_template( "customers.html", cfg = cfg, customers = customers )