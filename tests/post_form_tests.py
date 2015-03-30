from nose.tools import *
from tests.tools import assert_response
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
from post_form import app
def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/")
    assert_response(resp, status="404")

    # test our first GET request to /subscribe
    resp = app.request("/subscribe")
    assert_response(resp)

    # make sure default values work for the form
    resp = app.request("/subscribe", method="POST")
    assert_response(resp, contains="Nobody")

    # test that we get expected values
    data = {'username': 'alan','make': 'Toyota', 'model': 'Camry', 'email': 'test@ncsu.edu', 'minYear': '2007', 'maxYear': '2015', 'minPrice': '500', 'maxPrice': '100000', 'currentTime': 'tempcurrentTime'}
    resp = app.request("/subscribe", method="POST", data=data)
    assert_response(resp, contains="alan")
