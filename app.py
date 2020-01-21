import pymongo
from flask import request
from flask import jsonify
from bson.json_util import dumps
import flask


app = flask.Flask(__name__)
log = app.logger

client = pymongo.MongoClient("mongodb+srv://user01:bl4ck4dd3r@cluster0-kooqx.mongodb.net/test?retryWrites=true&w=majority")
db = client.sample_airbnb
collection = db.listingsAndReviews

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/v1/name/', methods=['GET'])
def api_all():
    name = request.args.get('name')
    result = collection.find({"name":name})
    return jsonify(dumps(result))





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
