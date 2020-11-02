from flask_restful import Resource
from flask import Response,request
import json
import pandas as pd

#return useful information
class Sample(Resource):
	def get(self):#block get method
		pass
	def post(self):#open post method
		print(json.loads(request.data)['mode'])#the data delivered from frontend to backend are stored in the request.data, which should be jsonfied.
		data=pd.read_csv("20200101.csv")
		orgX=list(data['org_latitude_deg'])
		orgY=list(data['org_longitude_deg'])
		dstX=list(data['dst_latitude_deg'])
		dstY=list(data['dst_longitude_deg'])
		routes=[]
		for i in range(len(orgX)):
			routes.append([[orgY[i],orgX[i],0],[dstY[i],dstX[i],0]])
		data = json.dumps({'routes':routes})
		res = Response(response=data, status=200, mimetype="application/json")#send message to frontend
		return res
