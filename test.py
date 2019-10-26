import os
import unittest
import bcrypt
import app as myapp
from app import app, page_not_found, password_check
from flask_pymongo import PyMongo

mongo = PyMongo(app)


class testApp(unittest.TestCase):

    """Set up and tear down"""
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = myapp.app.test_client()
        self.app.users = {}
        
        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    """
    Test suite for app.py
    """
    def test_is_working(self):
        self.assertEqual(1, 1)

    def test_page_not_found(self):
        response = self.app.get('404')
        self.assertEqual(response.status_code, 404)

    def test_about_page_route(self):
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
    
    def test_login_check_combination_logic_true(self):
        hashpass = bcrypt.hashpw('test'.encode('utf-8'), bcrypt.gensalt())
        db_password = hashpass.decode()
        result = password_check('test', db_password)
        self.assertTrue(result)
    
    def test_login_check_combination_logic_false(self):
        hashpass = bcrypt.hashpw('test'.encode('utf-8'), bcrypt.gensalt())
        db_password = hashpass.decode()
        result = password_check('testing', db_password)
        self.assertFalse(result)
      

if __name__ == "__main__":
    unittest.main()
