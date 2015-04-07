from nose.tools import *
from tools import assert_response
import os, sys
path = os.path.abspath(os.path.join('bin'))
sys.path.append(path)
from post_form import app
def test_index():


    # test our first GET request to /subscribe
    resp = app.request("/")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/", method="POST")
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'username': 'alan','make': 'Toyota', 'model': 'Camry', 'email': 'test@ncsu.edu', 'minYear': '2007', 'maxYear': '2015', 'minPrice': '500', 'maxPrice': '100000', 'currentTime': 'tempcurrentTime'}
    resp = app.request("/", method="POST", data=data)
    assert_response(resp, contains="alan")
