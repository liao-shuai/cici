# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pymongo

client = pymongo.MongoClient('119.23.203.236', 27017)
db = client.iot08
print db.name
