from flask_restful import Resource
from flask import Response,request
import json
import pandas as pd


date_list=list(range(20200101,20200132))
date_list+=list(range(20200201,20200230))
date_list+=list(range(20200301,20200332))
date_list+=list(range(20200401,20200431))
#return useful information
class Sample(Resource):
	def get(self):#block get method
		pass
	def post(self):#open post method
		flag=json.loads(request.data)['mode']
		print(flag)#the data delivered from frontend to backend are stored in the request.data, which should be jsonfied.
		data=None
		if flag==1:
			data = json.dumps({'date_list':date_list})
		elif flag==2:
			date=json.loads(request.data)['date']
			csv=pd.read_csv("./flight/"+str(date)+".csv")
			orgX=list(csv['org_latitude_deg'])
			orgY=list(csv['org_longitude_deg'])
			dstX=list(csv['dst_latitude_deg'])
			dstY=list(csv['dst_longitude_deg'])
			routes=[]
			for i in range(len(orgX)):
				routes.append([[orgY[i],orgX[i],0],[dstY[i],dstX[i],0]])
			data = json.dumps({'routes':routes})

		'''
		data=pd.read_csv("20200101.csv")
		orgX=list(data['org_latitude_deg'])
		orgY=list(data['org_longitude_deg'])
		dstX=list(data['dst_latitude_deg'])
		dstY=list(data['dst_longitude_deg'])
		routes=[]
		for i in range(len(orgX)):
			routes.append([[orgY[i],orgX[i],0],[dstY[i],dstX[i],0]])
		data = json.dumps({'routes':routes})
		'''
		res = Response(response=data, status=200, mimetype="application/json")#send message to frontend
		return res
