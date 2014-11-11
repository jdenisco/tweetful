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
import argparse

from urls import *


def friend_ids():
    """ friends function """
    try:
        auth = authorization.authorize()
        r = requests.get(FRIENDS_LIST, auth=auth)
        flist = json.loads(r.content)
        for ids in flist['ids']:
            print ids

    except (requests.exceptions.RequestException, Exception) as e:
        print e


def friend_id_2_name(id):
    """ Converts friends id into readable name """
    try:
        auth = authorization.authorize()
        rid = requests.get(FRIENDS_ID2NAME + '&user_id=' + id, auth=auth)
        rid_name = json.loads(rid.content)
        for name in rid_name:
            return name['name']

    except (requests.exceptions.RequestException, Exception) as e:
        print e


def trendingplaces(WOEID=1):
    """ Trending places """
    a = 0
    try:
        auth = authorization.authorize()
        rtrend = requests.get(TRENDS_PLACE + str(WOEID), auth=auth)
        rtrend_return = json.loads(rtrend.content)
        if 'errors' not in rtrend_return:
            for place in rtrend_return:
                while a < 10:
                    topic = place['trends'][a]['name']
                    urls = place['trends'][a]['url']
                    print("Trending Topics %s for more info %s " % (topic, str(urls)))
                    a += 1
            else:
                print('Error: %s' % rtrend_return['errors'][0]['message'])

    except (requests.exceptions.RequestException, Exception) as e:
        print e


def make_parser():
    """ Construct command line parser """
    description = "Get info from twitter"
    parser = argparse.ArgumentParser(description=description)
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    # Subparser for getting friends ids
    ids_parser = subparsers.add_parser('ids', help='List of all friends ids')
    iton_parser = subparsers.add_parser('iton', help='converts id into name')
    iton_parser.add_argument('id', help='id of the name you want to get', type=int)
    trends_parser = subparsers.add_parser('trendingplaces',  help='Trends by WOEID or default to global')
    trends_parser.add_argument("WOEID", default='1', nargs='?', type=int,  help='Yahoo! Where On Earth ID')

    return parser


def main():
    """ Main function """
    parser = make_parser()
    arguments = parser.parse_args()
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "trendingplaces":
        WOEID = int(arguments['WOEID'])

        print("Trending info")
        trendingplaces(WOEID)

    if command == 'ids':
        friend_ids()

    if command == 'iton':
        id = str(arguments['id'])
        print id
        print(friend_id_2_name(id))

if __name__ == "__main__":
    main()
