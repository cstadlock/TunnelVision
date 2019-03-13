from allImports import *

@app.route("/editTunnel/<ord_design_id>", methods = ["GET","POST"])
@login_required
def editTunnel(ord_design_id):
  """this function adds tunnels to an order after the order is being created"""
  page = request.path
  tunnel = OrderDesign.get(OrderDesign.ord_design_id==ord_design_id)
  designs = Design.select()

  if request.method == "GET":
    return render_template("editTunnel.html",
                           cfg = cfg,
                           tunnel=tunnel,
                           designs = designs)
  data = request.form    #returns dict of form info


  tunnel.design_nm = data["design"]
  tunnel.num_of_bows = data["num_of_bows"]
  tunnel.save()
  return redirect(url_for("editOrder", o_id = tunnel.order_id.o_id))