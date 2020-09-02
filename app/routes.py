from app import app
from flask import json, request

users_db = [
  {"id":1,"name":"John","age":"30"},
  {"id":2,"name":"Robert","age":"22"},
  {"id":3,"name":"Dorothy","age":"37"}
]

db_index = len(users_db)



@app.route('/')
@app.route('/index')
def index():
  return "REST API with Python"



@app.route('/api/users', methods=['GET'])
def users():
  return json.dumps(users_db)



@app.route('/api/users', methods=['POST'])
def usersPost():
  global db_index
  db_index += 1
  if "name" in request.args and "age" in request.args:
    users_db.append({"id":db_index,"name":request.args["name"],"age":request.args["age"]})
    return json.dumps(users_db)
  else:
    return {}


  
@app.route('/api/user/<id>', methods=['GET'])
def user(id):
  return json.dumps(list(filter(lambda x:int(x["id"])==int(id), users_db)))



@app.route('/api/user/<id>', methods=['POST'])
def userPost(id):
  for index, user in enumerate(users_db):
    if int(user["id"]) == int(id):
      if "name" in request.args:
        users_db[index]["name"] = request.args["name"]
      if "age" in request.args:
        users_db[index]["age"] = request.args["age"]
      return "updated "
  return {}
  
  

@app.route('/api/user/<id>', methods=['DELETE'])
def delete(id):
  for index, user in enumerate(users_db):
    if int(user["id"]) == int(id):
      del users_db[index]
      return "deleted "
  return {}

