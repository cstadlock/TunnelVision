from allImports import *

@app.route("/editOrder/<o_id>/addTunnel", methods = ["GET","POST"])
@login_required
def addTunnel(o_id):
  """this function adds tunnels to an order after the order is being created"""
  page = request.path
  designs = Design.select()
  o_id = int(o_id)
  if request.method == "GET":
    return render_template("addTunnels.html",
                           cfg = cfg,
                           num_tunnels = 1,
                           designs = designs)
  data = request.form    #returns dict of form info
  new_tunnel = OrderDesign.create(order_id = o_id,
                                design_nm = data["design_0"],
                                num_of_bows = data["num_of_bows_0"])
  new_tunnel.save()
  return redirect(url_for("editOrder", o_id = o_id))