from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from .models import Tickets
from .forms import TicketingForm

from info.models import SceneInfo

import qrcode
import os
from artcodian import settings

ROOT_URL = ''

def ticket(request):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data('Some data')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return HttpResponse(img)


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
            filename = 'tickets/' + post.id_code + '.png'
            post.qrcode_path = os.path.join(settings.MEDIA_ROOT, filename)
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(post.id_code)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save(post.qrcode_path)
            '''
            code here
            '''

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
