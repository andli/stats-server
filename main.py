#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a web server for collecting stats.
"""

__author__ = "Andreas Ehrlund"
__version__ = "0.1.9"
__license__ = "MIT"

import os
from datetime import datetime, timedelta

from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)
mdb_client = MongoClient(os.environ.get('MONGODB_URI', None, retryWrites=False))
db_name = os.environ.get('MONGODB_URI', None).rsplit('/', 1)[-1]
db = mdb_client[db_name]


@app.route('/pymkm', methods=['GET', 'POST'])
def pymkm():
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        if 'version' in json_data and 'command' in json_data:
            print('in')
            data = {
                'date': datetime.utcnow(),
                'version': json_data['version'],
                'uuid': json_data['uuid'],
                'command': json_data['command']
            }

            # store data row
            try:
                collection = db.reports
                collection.insert_one(data)
                print('stored')
            except Exception as err:
                resp = jsonify(success=False)
                print(err)
            else:
                resp = jsonify(success=True)
        else:
            resp = jsonify(success=False)

        return resp
    elif request.method == 'GET':
        delta = timedelta(days=365)
        date_stop = datetime.now() - delta
        try:
            collection = db.reports
            #print(f"count: {collection.count_documents({})}")
            result = collection.find({"date": {"$gt": date_stop}}, {'_id': False}).sort("date")
            res = list(result)
            return jsonify(res)
        except Exception as err:
            resp = jsonify(success=False)
            print(err)
