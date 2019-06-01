from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Tickets
from .forms import TicketingForm

from info.models import SceneInfo

import requests

import json
import xmltodict
# Create your views here.

def ticket(request):
    return HttpResponse("Let's check tickets")


def check_ticket(request, code):
    try:
        ticket = Tickets.objects.get(id_code=code)
    except Exception:
        return HttpResponse("Not Valid Code")
    else:
        if ticket.is_entered == False:
            ticket.is_entered=True
            ticket.save()
            return HttpResponse(code)
        else:
            return HttpResponse("already entered")


def ticket_generation(request):
    if request.method == "POST":
        form = TicketingForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False);
            post.pur_date = timezone.now()
            post.save()
            s_obj = get_object_or_404(SceneInfo, pk=post.scene.pk)
            s_obj.booked_seats += 1
            s_obj.vacant_seats = s_obj.total_seats - s_obj.booked_seats
            s_obj.save()
            return redirect('ticket')
        else:
            return HttpResponse("wrong data")
    else:
        pass
    form = TicketingForm()
    'vacant 받아오기 위해서는 앞 페이지에서 타고 들어가는 과정이 있어야'
    # vacant =
    return render(request, 'ticketing.html', {'form':form})

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
