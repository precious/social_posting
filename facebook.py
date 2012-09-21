#!/usr/bin/python

from settings import facebook_keys_dict
import urllib, urllib2

def make_post(text):
	url = 'https://graph.facebook.com/%s/feed' % facebook_keys_dict['user_id']
	post_dict = {'message': text,'access_token': facebook_keys_dict['access_token']}
	request = urllib2.Request(url, '&'.join(key + '=' + post_dict[key] for key in post_dict))

	try:
		response = urllib2.urlopen(request)
		return True
	except:
		return False
