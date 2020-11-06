from flask_restful import Resource
from flask import Response,request
import json
import pandas as pd
import networkx as nx

date_list=list(range(20200101,20200132))
date_list+=list(range(20200201,20200230))
date_list+=list(range(20200301,20200332))
date_list+=list(range(20200401,20200431))
def transform_format(date):
	date=str(date)
	return date[4:6]+"-"+date[6:8]
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
		elif flag==3:
			patterns=pd.read_csv("./flight/patterns.csv")
			patterns={"average_clustering":list(dict(patterns)["average_clustering"]),
			"transitivity":list(dict(patterns)["transitivity"]),
			"global_efficiency":list(dict(patterns)["global_efficiency"]),
			"reciprocity":list(dict(patterns)["reciprocity"]),
			"average_degree":list(dict(patterns)["average_degree"]),
			"nodes":list(dict(patterns)["nodes"]),
			"edges":list(dict(patterns)["edges"])}
			data = json.dumps({'patterns':patterns})
		elif flag==4:
			data=list(map(transform_format,date_list))
			data = json.dumps({'date_list':data})
		elif flag==5:
			date=json.loads(request.data)['date']
			attribute=int(json.loads(request.data)['attribute'])
			csv=pd.read_csv("./flight/"+str(date)+".csv")
			coords={}
			G=nx.DiGraph()
			for index, row in csv.iterrows():
				G.add_edge(row['origin'],row['destination'])
				coords[row['origin']]={'point':[row['org_latitude_deg'],row['org_longitude_deg']],'country':row['org_iso_country']}
				coords[row['destination']]={'point':[row['dst_latitude_deg'],row['dst_longitude_deg']],'country':row['dst_iso_country']}
			array=[]
			if attribute!=6:
				result=None
				if attribute==1:
					result=nx.closeness_centrality(G)
				elif attribute==2:
					result=nx.average_neighbor_degree(G)
				elif attribute==3:
					result=nx.degree_centrality(G)
				elif attribute==4:
					result=nx.pagerank(G)
				elif attribute==5:
					result=nx.hits(G)[0]
				for item in result.keys():
					array.append({'name':item,'value':[coords[item]['point'][1],coords[item]['point'][0],0],'index':result[item]})
			else:
				result=nx.degree(G)
				for item in result:
					array.append({'name':item[0],'value':[coords[item[0]]['point'][1],coords[item[0]]['point'][0],0],'index':item[1]})

			data = json.dumps({'array':array})
			print("handle sptial data finish")
		res = Response(response=data, status=200, mimetype="application/json")#send message to frontend
		return res
