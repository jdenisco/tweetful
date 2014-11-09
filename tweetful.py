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

def main():
    """ Main function """
    auth = authorization.authorize()

    response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)

if __name__ == "__main__":
    main()


