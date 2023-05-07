from flask import Flask
from flask import request,redirect,url_for
import json



app = Flask(__name__)



users = [{'id': 1, 'name': 'lidor', 'address': 'gedera'}, {'id': 2, 'name': 'roei', 'address': 'rishon'}, \
         {'id': 3, 'name': 'ofir', 'address': 'petachTekva'}, {'id': 4, 'name': 'vlad', 'address': 'tel aviv'}]


@app.route('/users', methods=['GET', 'POST'])
def getUsers():
    if request.method == 'GET':
        return json.dumps(users)
    elif request.method == 'POST':
        user = request.get_json()
        # user["id"]=request.form['id';
        # user["id"]=request;
        # user["id"]=re;
        print(user)
        users.append(user)
        return json.dumps(users)

@app.route('/userspost',methods=['POST'])
def postUser():
    temp=request.get_json()
    id=len(users)
    temp['id']=id
    users.append(temp)
    return redirect(url_for('getUSerById',id=temp['id']))

@app.route('/users/<int:id>', methods=['GET','DELETE','PUT'])
def getUSerById(id):
    if request.method=='GET':
        for js in users:
            if js['id'] == id:
                return json.dumps(users[id - 1])
        return 'we dont have this user '
    if request.method=='DELETE':
        updated=[user for user in users if user['id']!=id]
        return json.dumps(updated)
    if request.method=='PUT':
        newuser=request.get_json()
        for c in users:
            if c['id']==id:
                c['name']=newuser['name']
                c['address']=newuser['address']
        return json.dumps(users)




app.run(host="0.0.0.0", port=5010)
