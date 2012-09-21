#!/usr/bin/python

import urllib, urllib2
import md5
import time
import random
import json
from settings import vk_keys_dict

def make_post(text):
	api_url = 'https://api.vk.com/api.php'
	params_dict = {
		'api_id': vk_keys_dict['app_id'],
		'method': 'wall.post',
		'v': '3.0',
		'format': 'json',
		'owner_id': vk_keys_dict['user_id'],
		'message': text,
		'timestamp': str(int(time.time())),
		'random': str(random.randint(1,2**32)),
		'access_token': vk_keys_dict['access_token'],
	}

	# generating signature
	md5_source = ''.join(key + '=' + params_dict[key] for key in sorted(params_dict.keys()))
	md5_source  += vk_keys_dict['app_secure_key']
	params_dict['sig'] = md5.new(md5_source).hexdigest()

	request = urllib2.Request(api_url,urllib.urlencode(params_dict))
	try:
		response = urllib2.urlopen(request)
		if u'error' in json.load(response):
			return False
		return True
	except:
		return False
