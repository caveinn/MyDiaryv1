'''intilistaion file for flask app'''
from flask import Flask, jsonify, request , make_response
from instance.config import app_config
import uuid
from werkzeug.security import generate_password_hash, check_password_hash


#data models initialised with some files for testing
hashed_Password=generate_password_hash("1234", method="sha256")
entries={"1":{ "title":"example", "content":"some random stuff"}, "2":{ "title":"sample2", "content":"some other random stuff"}}
users={"1":{"username":"jane doe", "password":hashed_Password, "email":"janedoe@gmail.com"}}

#functions to add new items to the data models
def add_Entries_To_Db(id,title, content):
    temp_Entry={}
    temp_Entry["title"]=title
    temp_Entry["content"]=content
    entries[id]=temp_Entry

def add_Users_To_Db(id,username, password, email):
    temp_User={}
    temp_User["username"]=username
    temp_User["password"]=generate_password_hash(password,method="sha256")
    temp_User["email"]=email
    users[id]=temp_User

def create_App(config_name):
    '''Configuring the app'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')
    entry_Id_Counter=0
    @app.route('/')
    def index():
        '''What to see when visit site'''
        page="<h1>This is the landing page for my api</h1 \
                <p>You can test the various api endpoints which</p>\
                <ul><li>/api/v1/login</li><li>/api/v1/users<li> \
                <li>/api/v1/entries</li><li><h3>among others</li></ul>"
        return page
    @app.route('/api/v1/login')
    def login():
        authorization=request.authorization
        if not authorization or not authorization.username or not authorization.password:
            response=jsonify({"message":"failed to login"})
            response.status_code=401
            return response
        user=None
        for value in users.values():
            if value["username"]==authorization.username:
                user=value
        if not user:
            response=jsonify({"message":"failed to login"})
            response.status_code=401
            return response
        if check_password_hash(user["password"],authorization.password):
            response=jsonify({"Token":"token to be genereted"})
            return response
        response=jsonify({"message":"failed to login"})
        response.status.code=401
        return response

    @app.route('/api/v1/users', methods=['POST'])
    def create_User():
        '''Creating a new user'''
        data=request.get_json()
        if data:
            add_Users_To_Db(str(uuid.uuid4()), data['username'], data['password'], data['email'])
            response=jsonify({"message": "entry created succesfully"})
            response.status_code=201
            return response
        return jsonify({"message":"send data"})

    @app.route('/api/v1/entries', methods=['GET'])
    def get_All_Entries():
        '''Get all entries'''
        return jsonify(entries)

    @app.route('/api/v1/entries/<entryid>', methods=['GET'])
    def get_Single_Entry(entryid):
        '''Api endpoint to get a single entry'''
        if entryid in entries.keys():
            return jsonify({entryid:entries[entryid]})
        return jsonify({"message":"invalid id"})
    
    @app.route('/api/v1/entries', methods=['POST'])
    def create_Entry():
        ''''''
        data=request.get_json()
        if data:
            add_Entries_To_Db(str(uuid.uuid4()), data['title'], data['content'])
            response=jsonify({"message": "entry created succesfully"})
            response.status_code=201
            return response
        return jsonify({"message":"send data"})
    
    @app.route('/api/v1/entries/<entriesid>', methods=["PUT"])
    def edit_Entry(entriesid):
        '''edit a single entry'''
        data=request.get_json()
        if data:
            print(entries)
            entries[entriesid]["title"]=data["title"]
            entries[entriesid]["content"]=data["content"]
            response=jsonify({"message":"updated succesfully"})
            return response
        response =jsonify({"message":"could not update"})
        response.status_code=400
        return response
    
    @app.route('/api/v1/entries/<entriesid>', methods=["DELETE"])
    def delete_Entry(entriesid):
        '''deliting a single entry'''
        if entriesid in entries.keys():
            print(entries.keys())
            del entries[entriesid]
            response=jsonify({"message":"deleted succesfully"})
            response.status_code=204
            return response
        response=jsonify({"message":"failed to delete "})
        response.status_code=400
        return response

    return app
