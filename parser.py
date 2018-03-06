import os
import json
import urllib.parse
import urllib.request
import pprint
import sys

# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/BGUConfession/posts"
ACCESS_TOKEN = "EAACEdEose0cBAMbLZAXZAdhdmeenTszKX10NHG4yvFyZCZCErWfeoht55A1g0TRdjo8u7DoFnfZAhc9pVVxk8zEq3fg5beyoQgIkHKS9yd15oZB0LVtIyqviKPSEQ9nYTxEssyYkqZBkzF2ggWyQWcyu83YEZBiykdbxDWF4tbXGvGvl69nWg1LIHvRthmlG9ciZAnQgpmfbRjQZDZD"

def get_resp(host,path,params):
	url = "{host}{path}?{params}".format(host=host, path=path, params=params)
	resp = urllib.request.urlopen(url).read()
	me = json.loads(resp)
	return me

def get_likes(id):
	path = '/'+id+'/likes'
	params = urllib.parse.urlencode({"access_token": ACCESS_TOKEN,"summary":"true"})
	me = get_resp(host,path,params)
	return me['summary']['total_count']


arr = []
for i in range(0,100,6500):
	params = urllib.parse.urlencode({"access_token": ACCESS_TOKEN,"limit" : "100" , "offset":str(i)})
	me = get_resp(host,path,params)
	for post in me['data']:
		obj = (post['message'],get_likes(post['id']))
		print(obj)
		arr.append(obj)
		
pprint.pprint(arr[0][0])