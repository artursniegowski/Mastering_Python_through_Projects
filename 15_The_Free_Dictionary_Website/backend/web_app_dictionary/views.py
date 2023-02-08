from web_app_dictionary import (
    app, 
    current_year, 
    owl_api,
    )
from flask import (
    jsonify,
    )

# Flask routes
# getting back the current_year from the server
@app.route("/get-current-year")
def get_current_year():
    """returns the current year from the server
    """
    return jsonify(currentYear = current_year), 200

# getting data for the searched word
@app.route("/get/<string:word_or_phrase_to_search_for>")
def get_data_for_search(word_or_phrase_to_search_for):
    """returns data on the searched word, based on the results from the API 
    """
    word_to_search = str(word_or_phrase_to_search_for).strip()
    # checking the the word passed is not an empty string
    # if so return an error message
    if word_to_search:
        data = owl_api.get_data(word_or_phrase_to_search_for)
        return jsonify(data=data), 200
    else:
        #400 = Bad Request
        return jsonify(error={"Bad Request": "The string passed is an empty word"}) , 400


