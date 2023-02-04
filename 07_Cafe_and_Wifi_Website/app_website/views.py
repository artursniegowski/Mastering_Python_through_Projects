from app_website import app
from flask import render_template
from datetime import datetime
from app_website.models import Cafe, db

# current year - global variable
# current year
current_year = datetime.now().strftime("%Y")

# Flask routes
# home website
@app.route("/")
def index() -> str:

    # selecting all cafes
    all_cafes = db.session.execute(db.select(Cafe)).scalars()

    return render_template(
        'index.html',
        current_year = current_year,
        cafes = all_cafes,
    )
