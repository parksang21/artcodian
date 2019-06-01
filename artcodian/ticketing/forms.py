from django import forms

from .models import Tickets

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class TicketingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('title', 'scene',)
