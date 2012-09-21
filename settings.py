########## Twitter ##########
# create application here https://dev.twitter.com/apps and set for it permissions: Read and Write
twitter_tokens_dict = {
	'oauth_consumer_key': '',
	'oauth_token': '',
}

twitter_secrets_dict = {
	'oauth_consumer_secret': '',
	'oauth_token_secret': '',
}

########## Facebook ##########
# 1. Creating app
# create app here https://developers.facebook.com/apps and set for it
# Settings > Basic > Sandbox Mode: Enabled
# Settings > Persmissions > Extended Permissions: publish_stream, offline_access
# Settings > Advanced > Remove offline_access > disabled
# 2. Granting app permissions
# go to https://graph.facebook.com/oauth/authorize?client_id=APP_ID&scope=publish_stream,offline_access&redirect_uri=http://www.facebook.com/connect/login_success.html
# (dont forget to replace APP_ID with your own) and allow the required permissions. You should see page with 'Success' word.
# Copy the 'code' paramater from browser's address bar
# 3. Obtaining FB access_token for your app
# # 1st way
#   go to https://graph.facebook.com/oauth/access_token?client_id=APP_ID&redirect_uri=http://www.facebook.com/connect/login_success.html&client_secret=APP_SECRET&code=CODE
#   (dont forget to replace APP_ID, APP_SECRET with your own values and CODE by previously obtained 'code' parameter value)
#   open this url in your browser. You will see page with access_token.
# # 2nd way 
#   copy User Token from here: https://developers.facebook.com/tools/access_token/
# Paste your access_token here https://developers.facebook.com/tools/debug and make sure
# that is has expire date 'never'
 
facebook_keys_dict = {
	'app_id': '',
	'app_secret': '',
	# here should be access_token which never expires
	'access_token': '',
	'user_id': '',
}

########## Vk ##########
# create standalone app here http://vk.com/editapp?act=create
# go to http://api.vkontakte.ru/oauth/authorize?client_id=APP_ID&scope=wall,offline&redirect_uri=http://api.vkontakte.ru/blank.html&response_type=token
# (dont forget to replace APP_ID with your own) and allow the required permissions. You should see page with 'Login success' words.
# copy from browser's address bar access_token
vk_keys_dict = {
	'app_id': '',
	'app_secure_key': '',
	'user_id': '',
	'access_token': '',
}

try:
	from settings_local import *
except ImportError:
	pass
