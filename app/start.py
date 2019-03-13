# this renders the home page which is start.html
from allImports import *
@app.route("/old", methods = ["GET"])
@login_required
def start():
  return render_template("start.html",
                          cfg = cfg) # Do not worry about cfg, but you need
                                     # to pass that as an argument everytime
                                     # with render_template
                          