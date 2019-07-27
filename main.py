#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a web server for collecting stats.
"""

__author__ = "Andreas Ehrlund"
__version__ = "0.1.0"
__license__ = "MIT"

import sys
import csv
from datetime import datetime

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/pymkm', methods=['POST'])
def pymkm():
    json_data = request.get_json()
    if 'version' in json_data and 'command' in json_data:
        data = [datetime.utcnow(), json_data['version'], json_data['command']]

        with open('pymkm.csv', 'a', newline='') as fd:
            writer = csv.writer(fd)
            writer.writerow(data)

        resp = jsonify(success=True)
    else:
        resp = jsonify(success=False)

    return resp
