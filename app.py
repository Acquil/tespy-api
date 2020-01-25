
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
@app.route('/api/get/city/', methods=['GET'])
def get_city():
    name = request.args.get('name')
    result = collection.find({"city":name})
    op = []
    for obj in result:
        obj.pop('_id', None)
        op.append(obj)    
    
    return jsonify(op)

@app.route('/api/put/insert/', methods=['PUT'])
def insert_city_with_check():
    city = request.args.get('city')
    loc_x = request.args.get('loc_x')
    loc_y = request.args.get('loc_y')
    pop = request.args.get('pop')
    state = request.args.get('state')
    Zip = request.args.get('zip')

    if city and loc_x and loc_y and pop and state and Zip:
        result = collection.find({"city":city})
        op = []
        for obj in result:
            obj.pop('_id', None)
            obj.update({"ERROR": "City already exists"})
            op.append(obj)
        if op:
             return jsonify(op)
        else:
            test_json = {"city":city,"loc":{"x":loc_x,"y":loc_y},"pop":pop,"state":state,"zip":Zip}
            post_id = collection.insert_one(test_json).inserted_id
            return "<h1> Inserted Successfully "
    else:
        return "<h1> Please give all keys "

@app.route('/api/post/insert/', methods=['POST'])
def insert_city_without_check():
    city = request.args.get('city')
    loc_x = request.args.get('loc_x')
    loc_y = request.args.get('loc_y')
    pop = request.args.get('pop')
    state = request.args.get('state')
    Zip = request.args.get('zip')

    if city and loc_x and loc_y and pop and state and Zip:
       test_json = {"city":city,"loc":{"x":loc_x,"y":loc_y},"pop":pop,"state":state,"zip":Zip}
       post_id = collection.insert_one(test_json).inserted_id
       return "<h1> Inserted Successfully "

    else:
        return "<h1> Please give all keys "


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
