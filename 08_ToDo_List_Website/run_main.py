from app_website import app
from env_variables import FLASK_PORT

#### running the website ####
# running the app and setting the required env variable as a script
if __name__ == "__main__":
    # only run if it's not imported
    # so only if the file run_main.py is run directly and not imported
    # by another file

    # adding the env variable for Flask to work
    # > $env:FLASK_APP = "run_main"
    import os

    # print(os.environ.get("FLASK_APP"))
    os.environ["FLASK_APP"] = "run_main"

    # > flask run
    # start server
    # in a debug mode not suitable for production !!
    # Setting host='0.0.0.0' will make Flask available from the network)
    # Bind to PORT if defined, otherwise default to 5000.
    # TODO: set debug back to False before production!!!
    app.run(host='0.0.0.0', port=FLASK_PORT, debug=True)