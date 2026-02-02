from flask import Flask,jsonify,request
from appdb import Users
import requests

app = Flask(__name__)

user_instance = Users()

@app.route('/',methods=['GET'])
def view_users():
    return jsonify(user_instance.view())

@app.route('/adduser',methods=['POST'])
def add_user():

    data = request.get_json()

    name = data['name']
    email = data['email']

    viewusers = user_instance.view()
    if_match = next((v for v in viewusers if email == v['email']),None)

    if if_match:
        return jsonify({'message':'email already use'}),401
    user_instance.add(name,email)
    return jsonify({'messge':'Successfully added'}),201

@app.route('/updateuser',methods=['PUT'])
def update_user():
    data = request.get_json()
    id = data['id']
    name = data['name']
    email = data['email']

    viewusers = user_instance.view()

    if_match = next((v for v in viewusers if id == v['id']),None)

    if not if_match:
        return jsonify({'message':'Not found'}),404
    user_instance.update(name,email,id)
    return jsonify({'message':'update successfully'}),200

@app.route('/deleteuser',methods=['DELETE'])
def delete_user():
    data = request.get_json()
    id = data['id']
    # name = data['name']
    # email = data['email']

    viewusers = user_instance.view()
    if_match = next((v for v in viewusers if id == v['id']),None)

    if if_match:
        user_instance.delete(id)
        return jsonify({'message':'successfully deleted'})
    return jsonify({'message':'Not found'}),404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
