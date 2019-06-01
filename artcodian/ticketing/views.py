from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
import requests

import json
import xmltodict

key = 'f03ae19a6bed46fea2ee0637727e134c'

stdate = '20160101' 
eddate = '20190731'
cpage = '1'
rows = '10'

def index(request):
    return HttpResponse("asdf")

def show(request):
	place = []
	name = []
	s_id = []
	time = []

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

	return render(request, 'arcodian/show.html', {'s_id' : s_id, 'name':name, 'place':place, 'time':time})