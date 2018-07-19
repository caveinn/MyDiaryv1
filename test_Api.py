import unittest
import os
import json
#from instance.config import app_config
from app import create_App

class ApiTestCase(unittest.TestCase):
    '''This is a class for Api testcase'''

    def setUp(self):
        '''Initilise and setup the app'''
        self.app= create_App(config_name="testing")
        self.client= self.app.test_client 
        self.UserData={"username":"Jane doe", "email":"janedoe@gmail.com", "password":"sometext",}
        self.EntryData={"title": "myentry", "content":"something that doesnt really matter happened today"}
    
    def test_User_Creation(self):
        resp=self.client().post('/api/v1/user/', data=self.UserData)
        self.assertEqual(resp.status_code, 201)
    
    def test_Login(self):
        resp =self.client().post('/api/v1/user/login')
        self.assertEqual(resp.status_code, 200)

    def test_Create_Entry(self):
        resp=self.client().post('/api/v1/entry/', data=self.EntryData)
        self.assertEqual(resp.status_code, 201)

    def test_Get_All_Entries(self):
        resp= self.client().get('/api/v1/entries')
        self.assertEqual(resp.status_code, 200)

    def test_Get_Single_Entry(self):
        resp= self.client().get('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 200)

    def test_Delete_Entry(self):
        resp= self.client().delete('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 200)
    
    def tets_Modify_Entry(self):
        resp=self.client().put('/api/v1/entry/', data=self.EntryData)
        self.assertEqual(resp.status_code, 200)




if __name__ == '__main__':
    unittest.main()