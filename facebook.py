#!/usr/bin/python

from settings import facebook_keys_dict
import urllib, urllib2


# function return None if fails to retrieve access token
# def get_access_token():
# 	url = 'https://graph.facebook.com/oauth/access_token?client_id=%s&redirect_uri=http://www.facebook.com/connect/login_success.html&client_secret=%s&code=%s' % \
# 		(facebook_keys_dict['app_id'],facebook_keys_dict['app_secret'],facebook_keys_dict['code'])
# 	print 'url', url##################################
# 	try:
# 		response_str = urllib.urlopen(url).read()
# 		print response_str #################################
# 		if response_str.find('access_token=') == 0:
# 			return response_str[len('access_token='):]
# 	except:
# 		pass
	

def make_post(text):
	url = 'https://graph.facebook.com/%s/feed' % facebook_keys_dict['user_id']
	post_dict = {'message': text,'access_token': facebook_keys_dict['access_token']}
	request = urllib2.Request(url, '&'.join(key + '=' + post_dict[key] for key in post_dict))

	try:
		response = urllib2.urlopen(request)
		return True
	except:
		return False
