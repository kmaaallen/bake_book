import unittest
import app as myapp
from app import app, show_recipes, recipe_collection 
import os
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask import url_for, session

mongo = PyMongo(app)

class testApp(unittest.TestCase):

    """Set up and tear down"""
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = myapp.app.test_client()
 
        # Disable sending emails during unit testing
        self.assertEqual(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
    
    """
    Test suite for app.py
    """
    def test_is_suite_working(self):
        self.assertEqual(1, 1)

    def test_main_page_route(self):
        response = self.app.get('/show_recipes')
        self.assertEqual(response.status_code, 200)
  

if __name__ == "__main__":
    unittest.main()  