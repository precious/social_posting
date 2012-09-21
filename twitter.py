#!/usr/bin/python

from settings import twitter_tokens_dict, twitter_secrets_dict
import urllib, urllib2
import random
import string
import time
from hashlib import sha1
import hmac
import binascii


Q = lambda x: urllib.quote(x,'')

def get_hmac_sha1(key,raw_str):
    hashed = hmac.new(key, raw_str, sha1)
    return binascii.b2a_base64(hashed.digest())[:-1]


def make_tweet(text):
	base_url = 'https://api.twitter.com/1.1/statuses/update.json'
	http_method = 'POST'

	twitter_tokens_dict['oauth_nonce'] = ''.join(random.choice(string.ascii_uppercase + \
		string.ascii_lowercase + string.digits) for i in range(42))
	twitter_tokens_dict['oauth_timestamp'] = str(int(time.time()))
	twitter_tokens_dict['oauth_signature_method'] = 'HMAC-SHA1'
	twitter_tokens_dict['oauth_version'] = '1.0'
	
	# now its time to create signature
	params_dict = {'status': text}
	params_dict.update(twitter_tokens_dict)
	params = [(Q(key), Q(params_dict[key])) for key in sorted(params_dict.keys())]
	params_str = '&'.join(p[0] + '=' + p[1] for p in params) # urllib.urlencode isn't acceptable here
	signature_base_string = http_method + '&' + Q(base_url) + '&' + Q(params_str)
	signing_key = Q(twitter_secrets_dict['oauth_consumer_secret']) + '&' + \
		Q(twitter_secrets_dict['oauth_token_secret'])
	
	# phew. seems like we have the signature now
	twitter_tokens_dict['oauth_signature'] = get_hmac_sha1(signing_key,signature_base_string)
	header_str = 'OAuth ' + ', '.join(
		Q(key) + '="' + Q(twitter_tokens_dict[key]) + '"' for key in twitter_tokens_dict)

	post_data = 'status=' + Q(text)

	headers = {
		'Authorization': header_str,
		'Content-Length': str(len(post_data)),
	}
	
	request = urllib2.Request(base_url,post_data,headers)
	try:
		response = urllib2.urlopen(request)
		return True
	except:
		return False
