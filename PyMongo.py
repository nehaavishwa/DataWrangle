__author__ = 'nvishwakarma'

import bottle
import pymongo


@bottle.route('/')
def index():

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    db = connection.test()

    name = db.names

    item = name.find_one()

    return '<b>Hello %s</b>' % item['names']

bottle.run(host='127.0.0.1', port=8082)
