#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 10 14:20:16 2018

@author: shijie
"""

from flask import Flask, Response
from analysis import loadData, showRatingDistribution
data = loadData() 
app = Flask(__name__, static_url_path='', static_folder='.') 
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/vis/<platform>')
def hello(platform):
    df = data.get(platform,None)
    print("success!")
    response = ''
    if df is not None:
        response = showRatingDistribution(df,platform).to_json()
        
    return Response(response,
                    mimetype = 'application/json',
                    headers={
                            'Cache-Control': 'no-cache',
                            'Access-Control-Allow-Origin': '*'
                            }
                    )

if __name__ == '__main__': 
    app.run(port=8000)
