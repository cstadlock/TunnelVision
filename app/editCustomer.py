from allImports import *

@app.route("/editCustomer/<c_id>", methods = ["GET","POST"])
@login_required
def editCustomer(c_id):
  """this function adds tunnels to an order after the order is being created"""
  page = request.path
  customer = Customer.get(Customer.c_id==c_id)
  if request.method == "GET":
    return render_template("editCustomer.html",
                           cfg = cfg,
                           customer =customer)
  data = request.form    #returns dict of form info


  customer.first_name = data["firstname"]
  customer.last_name = data["lastname"]
  customer.email = data["email"]
  customer.phone_number = data["phonenumber"]
  customer.address = data["address"]
  customer.save()
  return redirect(url_for("customers"))