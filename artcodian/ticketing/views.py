from django.shortcuts import render
from django.utils import timezone

from django.http import HttpResponse
import requests
# Create your views here.

import json
import xmltodict

key = 'f03ae19a6bed46fea2ee0637727e134c'


def index(request):
    return HttpResponse("asdf")

def show(request):
	response = requests.get('http://www.kopis.or.kr/openApi/restful/pblprfr/PF132236?service='+key).text
	data = xmltodict.parse(response)
	
	return render(request, 'arcodian/show.html', 
		{'s_id': data['dbs']['db']['mt20id'],'name': data['dbs']['db']['prfnm'], 'place': data['dbs']['db']['fcltynm']})

