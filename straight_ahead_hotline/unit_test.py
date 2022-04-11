import pytest
import unittest
from __init__ import create_app
from flask import Flask


# def test_base_route():
    # app = Flask(__name__)
    # configure_routes(app)
    # client = create_app.test_client()
    # url = '/'

    # response = client.get(url)
    # assert response.status_code == 200



class FlaskTest(unittest.TestCase):
    # Check for response 200
    def test_index(self):
        tester = create_app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    if __name__ == '__main__':
        unittest.main()

