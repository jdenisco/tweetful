#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: tweetful
#   date: 2014-11-09
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import authorization

import json
import requests

from urls import *


def friend_ids():
    """ friends function """
    try:
        auth = authorization.authorize()
        r = requests.get(FRIENDS_LIST, auth=auth)
        flist = json.loads(r.content)
        for ids in flist['ids']:
            print ids

    except (requests.exceptions.RequestException,Exception) as e:
      print e 
    
def friend_id_2_name(id):
    """ Converts friends id into readable name """
    try:
        auth = authorization.authorize()
        rid = requests.get(FRIENDS_ID2NAME + '&user_id=' + id, auth=auth)
        rid_name = json.loads(rid.content)
        for name in rid_name:
            return name['name']

    except (requests.exceptions.RequestException,Exception) as e:
      print e 

def trendingplaces(WOEID=1):
    """ Trending places """
    a = 0
    try:
        auth = authorization.authorize()
        rtrend = requests.get(TRENDS_PLACE + str(WOEID), auth=auth)
        rtrend_return = json.loads(rtrend.content)
        for place in rtrend_return:
            while True: 
                if place['trends'][a]['name'] > 0 :
                    topic = place['trends'][a]['name']
                    urls = place['trends'][a]['url']
                    print type(urls)
                    print("Trending Topics %s for more info %s " % (topic, str(urls)))
                    a += 1
                else:
                   print "done"

    except (requests.exceptions.RequestException,Exception) as e:
      print e 

def main():
    """ Main function """
#    auth = authorization.authorize()

#    response = requests.get(TIMELINE_URL, auth=auth)
#    print json.dumps(response.json(), indent=4)

    friend_ids()
    print(friend_id_2_name('18936345'))
    trendingplaces()


if __name__ == "__main__":
    main()
