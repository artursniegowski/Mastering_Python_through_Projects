# custom decorators
# https://docs.python.org/3/library/functools.html#functools.wraps
from flask import redirect, url_for, Response
from flask_login import current_user
from functools import wraps

# checking if current user is logged in / authenticated, if not redirect to the given url
def user_logged_or_redirect(redirect_url: str = 'index') -> Response | str:
    """
    checking if current user is logged in / authenticated , if not redirect to the given url
    """
    def outter_wrapper(fn):
        @wraps(fn)
        def decorated_function(*args,**kwargs):
            if current_user.is_authenticated:
                return fn(*args,**kwargs)
            else:
                return redirect(url_for(redirect_url))

        return decorated_function
    return outter_wrapper
