from allImports import *

@app.route("/add/<num_tunnels>/tunnels/<o_id>", methods = ["GET","POST"])
@login_required
def createOrderTunnel(o_id, num_tunnels):
  """this function adds tunnels to an order after the order is being created"""
  page = request.path
  designs = Design.select()
  num_tunnels = int(num_tunnels)
  o_id = int(o_id)
  if request.method == "GET":
    return render_template("addTunnels.html",
                           cfg = cfg,
                           num_tunnels = num_tunnels,
                           designs = designs)
  data = request.form    #returns dict of form info
  for tunnel in range(num_tunnels):
    new_tunnel = OrderDesign.create(order_id = o_id,
                                    design_nm = data["design_"+ str(tunnel)],
                                    num_of_bows = data["num_of_bows_"+ str(tunnel)])
    new_tunnel.save()
    
  return redirect(url_for("orders"))
  
  #tunnel_source = []
  #turn data dict to list of dict for each record to be created
  #for tunnel in range(num_tunnels):
    #design_k = "design_" +str(tunnel)
    #bow_k = "num_of_bows_"+str(tunnel)
    #tunnel = {"design_nm": data[design_k], "num_of_bows" :data[bow_k], "order_id": o_id}  #hash with tunnel attributes
    #tunnel_source.append(tunnel)  #add to list of records
  #with db.atomic():
    #tunnels = OrderDesign.insert_many(tunnel_source).execute()
  #if tunnels.save():