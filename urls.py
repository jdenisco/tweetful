#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: urls
#   date: 2014-11-09
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
FRIENDS_LIST= API_URL + "/1.1/friends/ids.json?cursor=-1&screen_name=jimdenisco&count=5000"
FRIENDS_ID2NAME = API_URL + "/1.1/users/lookup.json?screen_name=jimdenisco,twitter"
TRENDS_PLACE = API_URL + '/1.1/trends/place.json?id='
