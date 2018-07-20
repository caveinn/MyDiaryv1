import unittest
import json

#from instance.config import app_config
from app import create_App

class ApiTestCase(unittest.TestCase):
    '''This is a class for Api testcase'''

    def setUp(self):
        '''Initilise and setup the app'''
        self.app=create_App(config_name="testing")
        self.client=self.app.test_client
        self.UserData=json.dumps({
                                "username":"Jane doe",
                                "email":"janedoe@gmail.com", 
                                "password":"sometext",
                                })
        self.EntryData=json.dumps({
                                "title": "myentry", 
                                "content": "something that doesnt really matter happened today"
                                })
    def test_User_Creation(self):
        '''Test the creation of users'''
        resp=self.client().post('/api/v1/users', data=self.UserData,content_type = 'application/json')
        self.assertEqual(resp.status_code, 201)
    
    def test_Login(self):
        '''Test user login endpoint'''
        resp =self.client().get('/api/v1/login', headers = {
                        'content-type': "application/json",
                        'authorization': "Basic amFuZSBkb2U6MTIzNA==",
                        })
        self.assertEqual(resp.status_code, 200)

    def test_Create_Entry(self):
        '''Test creation of a new entry'''
        resp=self.client().post('/api/v1/entries', data=self.EntryData,content_type = 'application/json')
        print(self.EntryData)
        self.assertEqual(resp.status_code, 201)

    def test_Get_All_Entries(self):
        '''Test if you can get all entries'''
        resp= self.client().get('/api/v1/entries')
        self.assertEqual(resp.status_code, 200)

    def test_Get_Single_Entry(self):
        '''Test for getting a single entry'''
        resp= self.client().get('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 200)
    
    def test_Modify_Entry(self):
        '''Teat for Modifying an entry'''
        resp=self.client().put('/api/v1/entries/2', data=self.EntryData,content_type = 'application/json')
        self.assertEqual(resp.status_code, 200)

    def test_Delete_Entry(self):
        '''Test for deleting an entry'''
        resp= self.client().delete('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 204)

if __name__ == '__main__':
    unittest.main()