# RPC: SERVER

# This Project borrows a bit of knowledge from various articles, projects, crypto sites, YouTube, tutorials, research papers. This may simply be a model

# This is the first take of the RPC server I have tried to replicate


from flask import Flask, jsonify, request
import time
import psutil
import json
import dicttoxml


app = Flask('__name__')
app.debug = True

# TIME PAGE
@app.route('/time')
def time_used():
    return jsonify(time=int(time.time()))


# VM Page


@app.route('/ram')
def ram_used():
    return jsonify(total=psutil.virtual_memory()[0], used=psutil.virtual_memory()[3])


# add data

@app.route('/add')
def add_data():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify(result=(a + b))



# SUB DATA

@app.route('/sub')
def sub_data():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify(result=(a - b))


# CONVERT TO XML

@app.route('/xml')
def xml_conversion():
    json_str = request.args.get('json_str', type=str)
    obj = json.loads(json_str)
    xml = dicttoxml.dicttoxml(obj)
    return jsonify(result=xml)

# USE TCP PORT 8088

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088)