
import pymongo
from flask import request
from flask import jsonify
from bson.json_util import dumps
import flask

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
log = app.logger

client = pymongo.MongoClient("mongodb+srv://user01:bl4ck4dd3r@cluster0-kooqx.mongodb.net/test?retryWrites=true&w=majority")
db = client.sample_training
collection = db.zips


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


# A route to return all of the available entries in our catalog.
@app.route('/api/city/', methods=['GET'])
def api_all():
    name = request.args.get('name')
    result = collection.find({"city":name})
    op = []
    for obj in result:
        obj.pop('_id', None)
        op.append(obj)    
    
    return jsonify(op)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
