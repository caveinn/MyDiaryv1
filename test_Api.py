import unittest
import json

from app import create_App

class ApiTestCase(unittest.TestCase):
    '''Check if various endpoints work well'''

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
        '''check if a user is created successfully'''
        resp=self.client().post('/api/v1/users', data=self.UserData,content_type = 'application/json')
        self.assertEqual(resp.status_code, 201)
    
    def test_Login(self):
        '''checking if user gets a token'''
        resp =self.client().get('/api/v1/login', headers = {
                        'content-type': "application/json",
                        'authorization': "Basic amFuZSBkb2U6MTIzNA==",
                        })
        self.assertEqual(resp.status_code, 200)

    def test_Login_No_Auth(self):
        '''checking if user gets a token'''
        resp =self.client().get('/api/v1/login')
        self.assertEqual(resp.status_code, 401)

    def test_Create_Entry(self):
        '''Checking that an entry was created successfully'''
        resp=self.client().post('/api/v1/entries', data=self.EntryData,content_type = 'application/json')
        print(self.EntryData)
        self.assertEqual(resp.status_code, 201)

    def test_Get_All_Entries(self):
        '''check if all entries are returned'''
        resp= self.client().get('/api/v1/entries')
        self.assertEqual(resp.status_code, 200)

    def test_Get_Single_Entry(self):
        '''Test for getting a single entry'''
        resp= self.client().get('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 200)
    
    def test_Modify_Entry(self):
        '''check that entry was modified succesfully'''
        resp=self.client().put('/api/v1/entries/2', data=self.EntryData,content_type = 'application/json')
        self.assertEqual(resp.status_code, 200)

    def test_Modify_Entry_Wrong_Id(self):
        '''check that entry was modified succesfully'''
        resp=self.client().put('/api/v1/entries/2')
        self.assertEqual(resp.status_code, 400)

    def test_Delete_Entry(self):
        '''check that entyr was deleted succesfully'''
        resp= self.client().delete('/api/v1/entries/1')
        self.assertEqual(resp.status_code, 204)
    #when user enters wron id
    def test_Delete_Entry_Wrong_Id(self):
        '''check that entyr id was not found'''
        resp= self.client().delete('/api/v1/entries/1232')
        self.assertEqual(resp.status_code, 400)


if __name__ == '__main__':
    unittest.main()