'''intilistaion file for flask app'''
from flask import Flask, jsonify, request , make_response
from instance.config import app_config
import uuid


entries={"1":{ "title":"example", "content":"some random stuff"}}
users={"1":{"username":"jane doe", "password":"1234", "email":"janedoe@gmail.com"}}

def add_Entries_To_Db(id,title, content):
    temp_Entry={}
    temp_Entry["title"]=title
    temp_Entry["content"]=content
    entries[id]=temp_Entry

def create_App(config_name):
    '''Configuring the app'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')
    entry_Id_Counter=0

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
        data=request.get_json()
        if data:
            add_Entries_To_Db(str(uuid.uuid4()), data['title'], data['content'])
            response=jsonify({"message": "entry created succesfully"})
            response.status_code=201
            return response
        return jsonify({"message":"send data"})


    return app
