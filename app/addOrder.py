from allImports import *

@app.route("/addOrder", methods = ["GET", "POST"])
@login_required
def createOrders():
  page = request.path
  if request.method == "GET":    #return view when request method is GET
    customers = Customer.select()
    statuses = Status.select()
    return render_template("addOrder.html",
                            cfg = cfg,
                            customers = customers,
                            statuses = statuses)
  data = request.form #returns dict of post data
  #for myval in data:
  #  print "*****"
  #  print myval
  #  print data[str(myval)]
  order = Order.create(customer = data["customer"], 
                 price = data["Price"],
                 status = data["status"],
                 notes = data["ordNotes"])
  num_tunnels = data["num_of_tuns"]
  #print num_tunnels
  order.save()    #if the order is created
  #print "gets here"
  #print order.o_id  #works, has id
  return redirect(url_for("createOrderTunnel", o_id = order.o_id, num_tunnels = num_tunnels))
  #else:
    #return "save failed"