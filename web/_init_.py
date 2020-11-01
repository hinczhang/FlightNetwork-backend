from flask import Flask, request, redirect, url_for
from flask_restful import Api
from flask_cors import CORS

#start import block; free edit
from web.resource.sample import Sample

#end import block

app = Flask(__name__)
CORS(app, supports_credentials=True) # CORS handle

'''add api resource'''
api = Api(app)

#start mode-use block; free edit
api.add_resource(Sample, '/api/index')

#end mode-use block
