from allImports import * # goes on top
#decorator
@app.route("/addCustomer" , methods = ["GET", "POST"])
@login_required
def addnewCustomer():
    
    page = request.path 
    if request.method == "GET":
        """This function will get data from the database"""
        customer = Customer.select()
        return render_template( "addCustomer.html", cfg = cfg, customer = customer )
    
    data = request.form #returns dict of post data
    thrNewCustomer = Customer.create (first_name = data["firstname"], last_name = data["lastname"], email = data["email"], phone_number = data["phonenumber"], address = data["address"]) #This Saves All Of The Data You Insert.
    
    return redirect(url_for("customers"))    