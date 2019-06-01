from django import forms

from .models import Tickets

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class TicketingForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ('title', 'scene',)

    def __init__( self, *args, **kwargs ):
        super( TicketingForm, self ).__init__( *args, **kwargs )
        self.fields[ 'title' ].widget.attrs.update( {
            'class': 'form-control',
            'id': 'id_title',
            'placeholder': 'Enter numbers' } )
        self.fields['scene'].widget.attrs.update({
            'class':'form-control',
        })
