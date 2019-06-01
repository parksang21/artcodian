from django.shortcuts import render

import requests
import json
import xmltodict


key = 'f03ae19a6bed46fea2ee0637727e134c'

stdate = '20160101'
eddate = '20190731'
cpage = '1'
rows = '10'

def show(request):
	place = []
	name = []
	s_id = []
	time = []
	seat = []

	response = requests.get('http://www.kopis.or.kr/openApi/restful/pblprfr?service='+key+'&stdate='+stdate+'&eddate='+eddate+'&cpage='+cpage+'&rows='+rows+'&prfstate=02').text
	r_data = xmltodict.parse(response)

	datas = r_data['dbs']['db']

	for i in range(len(datas)):
		s_id.append(datas[i]['mt20id'])
		name.append(datas[i]['prfnm'])
		place.append(datas[i]['fcltynm'])

	for i in range(len(s_id)):
		resp = requests.get('http://www.kopis.or.kr/openApi/restful/pblprfr/'+s_id[i]+'?service='+key).text
		r_d = xmltodict.parse(resp)
		data = r_d['dbs']['db']['dtguidance']
		time.append(data)

	for i in range(len(place)):
		res = requests.get('http://www.kopis.or.kr/openApi/restful/prfplc?service='+key+'&cpage='+cpage+'&rows='+rows+'&shprfnmfct='+place[i]).text
		r = xmltodict.parse(res)
		d = r['dbs']['db']['seatscale']
		seat.append(d)

	return render(request, 'arcodian/show.html', {'s_id' : s_id, 'name':name, 'place':place, 'time':time, 'seat':seat})

