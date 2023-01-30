from app_website import app
from flask import render_template

# 405 error handler - Method Not Allowed
@app.errorhandler(405)
def page_method_not_allowed(errors) -> str:
    """
    renders the 405 error page
    """
    # note that we set the 405 status explicitly
    return render_template("405.html"), 405

# 404 error handler - page not found
@app.errorhandler(404)
def page_not_founnd(errors) -> str:
    """
    renders the 404 error page
    """
    # note that we set the 404 status explicitly
    return render_template("404.html"), 404

# 403 error handler - forbidden
@app.errorhandler(403)
def page_forbidden(errors) -> str:
    """
    renders the 403 error page
    """
    # note that we set the 403 status explicitly
    return render_template("403.html"), 403