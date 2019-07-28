#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a web server for collecting stats.
"""

__author__ = "Andreas Ehrlund"
__version__ = "0.1.0"
__license__ = "MIT"

import os
from datetime import datetime

from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient

app = Flask(__name__)
mdb_client = MongoClient(os.environ.get('MONGODB_URI', None))

@app.route('/pymkm', methods=['POST'])
def pymkm():
    json_data = request.get_json()
    if 'version' in json_data and 'command' in json_data:
        data = {
            'date': datetime.utcnow(),
            'version': json_data['version'],
            'command': json_data['command']
        }

        # store data row
        try:
            db = mdb_client.pymkm
            collection = db.reports
            collection.insert_one(data)
        except Exception as err:
            resp = jsonify(success=False)
            print(err)
        else:
            resp = jsonify(success=True)
    else:
        resp = jsonify(success=False)

    return resp
