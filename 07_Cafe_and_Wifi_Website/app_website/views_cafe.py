from app_website import app
from flask import flash, jsonify, render_template, redirect, url_for, Response
from flask_login import current_user, login_required
from app_website.views import current_year
from app_website.models import Cafe, db
from app_website.forms import AddCafeForm


# Flask routes
# add cafe
@app.route("/add_cafe", methods = ['GET','POST'])
def add_cafe() -> Response | str :

    # checking if the user is logged in
    if not current_user.is_authenticated:
        # flash messages are valid only for one session!
        flash("ONLY logged in users can add a Cafe!")
        return redirect(url_for('login'))
    
    add_cafe_form = AddCafeForm(
        coffee_price="2.0-5.0", 
        price_currency="£",
        seats="20-30",
        )

     # if form is validated then it has to be a POST request
    if add_cafe_form.validate_on_submit():
        

        # checking if the cafe exists in the databse
        cafe_exists = db.session.execute(
            db.select(Cafe).filter_by(name=add_cafe_form.name.data.strip())
        ).scalar() # returns None if not found

        # if cafe dosent exists it will be added to the database
        if not cafe_exists:

            # create a new instance of a Cafe
            new_cafe = Cafe(
                name = add_cafe_form.name.data.strip(),
                map_url = add_cafe_form.map_url.data.strip(),
                img_url = add_cafe_form.img_url.data.strip(),
                location = add_cafe_form.location.data.strip(),
                has_sockets = add_cafe_form.has_sockets.data,
                has_toilet = add_cafe_form.has_toilet.data,
                has_wifi = add_cafe_form.has_wifi.data,
                can_take_calls = add_cafe_form.can_take_calls.data,
                seats = add_cafe_form.seats.data,
                coffee_price =  add_cafe_form.price_currency.data + add_cafe_form.coffee_price.data,
                cafe_creator = current_user,
            )

            # saving the new cafe to the database
            db.session.add(new_cafe)
            db.session.commit()

            # flash messages are valid only for one session!
            flash(f"Café {add_cafe_form.name.data.strip()} was successfully added.")
            # back to home
            return redirect(url_for('index'))


        # the cafe name already exists in the database
        else:
            # flash messages are valid only for one session!
            flash("A Café with that name already exists!")


    return render_template(
        'add_cafe.html',
        current_year = current_year,
        form = add_cafe_form,
    )

# delete cafe - and redirect with JavaScript
@app.route("/delete_cafe/<cafe_name>", methods = ['DELETE'])
@login_required
def delete_cafe(cafe_name: str) -> Response | str :

    # checking if the cafe exists in the databse
    cafe_exists = db.one_or_404(
            db.select(Cafe).filter_by(name=cafe_name)
        ) # returns None if not found

    # if cafe exists delete it otherwise sucess will be false
    # and javascript wont redirect the page
    if cafe_exists:
        db.session.delete(cafe_exists)
        db.session.commit()
        cafe_deleted = 'true'
    else:
        cafe_deleted = 'false'

    return jsonify(
        success=cafe_deleted,
        url_redirect=url_for('index'),
    )