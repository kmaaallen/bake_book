{"changed":true,"filter":false,"title":"test.py","tooltip":"/test.py","value":"import os\nimport unittest\nimport app as myapp\nfrom app import app, page_not_found\nfrom flask_pymongo import PyMongo\n\nmongo = PyMongo(app)\n\n\nclass testApp(unittest.TestCase):\n\n    \"\"\"Set up and tear down\"\"\"\n    # executed prior to each test\n    def setUp(self):\n        app.config['TESTING'] = True\n        app.config['WTF_CSRF_ENABLED'] = False\n        app.config['DEBUG'] = False\n        self.app = myapp.app.test_client()\n\n        # Disable sending emails during unit testing\n        self.assertEqual(app.debug, False)\n\n    # executed after each test\n    def tearDown(self):\n        pass\n\n    \"\"\"\n    Test suite for app.py\n    \"\"\"\n    def test_is_working(self):\n        self.assertEqual(1, 1)\n\n    def test_page_not_found(self):\n        response = self.app.get('404')\n        self.assertEqual(response.status_code, 404)\n\n    def test_about_page_route(self):\n        response = self.app.get('/about')\n        self.assertEqual(response.status_code, 200)\n\nif __name__ == \"__main__\":\n    unittest.main()\n","undoManager":{"mark":-2,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":40,"column":21},"action":"remove","lines":["import os","import unittest","import app as myapp","from app import app, page_not_found","from flask_pymongo import PyMongo","","mongo = PyMongo(app)","","class testApp(unittest.TestCase):","","    \"\"\"Set up and tear down\"\"\"","    # executed prior to each test","    def setUp(self):","        app.config['TESTING'] = True","        app.config['WTF_CSRF_ENABLED'] = False","        app.config['DEBUG'] = False","        self.app = myapp.app.test_client()"," ","        # Disable sending emails during unit testing","        self.assertEqual(app.debug, False)"," ","    # executed after each test","    def tearDown(self):","        pass","    ","    \"\"\"","    Test suite for app.py","    \"\"\"","    def test_is_working(self):","        self.assertEqual(1, 1)","        ","    def test_page_not_found(self):","        response = self.app.get('404')","        self.assertEqual(response.status_code, 404)","    ","    def test_about_page_route(self):","        response = self.app.get('/about')","        self.assertEqual(response.status_code, 200)","","if __name__ == \"__main__\":","    unittest.main()  "],"id":2},{"start":{"row":0,"column":0},"end":{"row":42,"column":0},"action":"insert","lines":["import os","import unittest","import app as myapp","from app import app, page_not_found","from flask_pymongo import PyMongo","","mongo = PyMongo(app)","","","class testApp(unittest.TestCase):","","    \"\"\"Set up and tear down\"\"\"","    # executed prior to each test","    def setUp(self):","        app.config['TESTING'] = True","        app.config['WTF_CSRF_ENABLED'] = False","        app.config['DEBUG'] = False","        self.app = myapp.app.test_client()","","        # Disable sending emails during unit testing","        self.assertEqual(app.debug, False)","","    # executed after each test","    def tearDown(self):","        pass","","    \"\"\"","    Test suite for app.py","    \"\"\"","    def test_is_working(self):","        self.assertEqual(1, 1)","","    def test_page_not_found(self):","        response = self.app.get('404')","        self.assertEqual(response.status_code, 404)","","    def test_about_page_route(self):","        response = self.app.get('/about')","        self.assertEqual(response.status_code, 200)","","if __name__ == \"__main__\":","    unittest.main()",""]}]]},"ace":{"folds":[],"scrolltop":308,"scrollleft":0,"selection":{"start":{"row":42,"column":0},"end":{"row":42,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":18,"state":"start","mode":"ace/mode/python"}},"timestamp":1571599466643}