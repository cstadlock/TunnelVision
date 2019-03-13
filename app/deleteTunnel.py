from allImports import *

@app.route("/<o_id>/deleteTunnel/<ord_design_id>", methods = ["GET","POST"])
@login_required
def deleteTunnel(o_id, ord_design_id):
  """this function deletes a tunnel from an order"""
  page = request.path
  o_id = int(o_id)
  tunnel = OrderDesign.get(OrderDesign.ord_design_id==ord_design_id)
  if request.method == "GET":
    return render_template("deleteTunnel.html",
                           o_id = o_id,
                           cfg = cfg)
  data = request.form    #returns dict of form info
  tunnel.delete_instance()
  return redirect(url_for("editOrder", o_id = o_id))