from allImports import *
from forms import DesignForm

@app.route("/designs", methods=["GET", "POST"])
@login_required
def design_components():
    designs = Design.select()
    design_form = DesignForm(request.form)
    if design_form.validate_on_submit():
        print "hello"
        bow_type = design_form.bow_type.data
        design_name = design_form.design_name.data
        inventory = design_form.inventory.data
        amountNeeded = design_form.amountNeeded.data
        Bow(bow_type=bow_type, design_name=design_name,
            inventory=inventory, amountNeeded=amountNeeded).save()
    
    
    return render_template("design.html", 
                                design_form=design_form,
                                designs = designs,
                                cfg = cfg)
    
    
@app.route("/delete/bow_component/<int:b_id>", methods=["GET"])
def delete_bow_component(b_id):
    bow_component = Bow.get(Bow.b_id==b_id)
    bow_component.delete_instance(recursive=True, delete_nullable=True)
    return redirect(url_for("design_components"))