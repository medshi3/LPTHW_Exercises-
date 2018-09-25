from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_indes():
	#chech that we get a 404 on the / URL
	resp = app.request("/")
	assert_response(resp, status="404")
	
	#test out first GET request to /hello
	resp = app.request("/hello")
	
	#make sure default values work for the format
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")
	
	#test that we get expected values
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	assert_response(resp, contains="Zed")
	