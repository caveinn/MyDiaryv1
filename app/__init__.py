'''intilistaion file for flask app'''
from flask import Flask, jsonify 
from instance.config import app_config

entry_Id_Counter=0 #count the number of entries and use it as customer_id
user_ID_Counter=0 #count the number of entries and use it as customer_id
entries={1:{ "title":"example", "content":"some random stuff"}}
users=[]

def add_Entries_To_Db(title, content):
    temp_Entry={}
    entry_Id_Counter+=1
    temp_Entry["id"]=entry_Id_Counter
    temp_Entry["title"]=title
    temp_Entry["content"]=content
    entries.append(temp_Entry)




def create_App(config_name):
    '''Configuring the app'''
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    @app.route('/api/v1/entries', methods=['GET'])
    def get_All_Entries():
        return jsonify(users)

    @app.route('/api/v1/entries/<entryid>', methods=['GET'])
    def get_Single_Entry(entryid):
        if entryid in entries.keys():
            return jsonify({entryid:entries[entryid]})
        return jsonify({"message":"invalid id"})


    return app
