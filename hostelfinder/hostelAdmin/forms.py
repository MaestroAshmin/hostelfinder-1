from django.forms import  ModelForm
from django import forms
from hostelAdmin.models import Geography, Hostel, Room, Fee,Image

class HostelForm(ModelForm):
    class Meta:
        model=Hostel
        fields = ['hostel_name','hostel_type','hostel_phone','hostel_mobile']
        widgets = {
            'hostel_name': forms.TextInput(attrs={'style': 'width:100%;'}),
            'hostel_type': forms.Select(attrs={'style': 'width:150px'}),
            'hostel_phone': forms.TextInput(attrs={'style': 'width:200px'}),
            'hostel_mobile': forms.TextInput(attrs={'style': 'width:200px'}),
        }

class GeographyForm(ModelForm):
    class Meta:
        model = Geography
        fields = ['location','latitude','longitude','additional']
        widgets = {
            'location': forms.Select(attrs={'style': 'width:350px'}),
            'latitude': forms.TextInput(attrs={'style': 'width:150px'}),
            'longitude': forms.TextInput(attrs={'style': 'width:150px'}),
            'additional': forms.TextInput(attrs={'style': 'width:250px'}),
        }

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['seater_type','quantity','room_price']

class FeeForm(ModelForm):
    class Meta:
        model = Fee
        fields = ['admission_fee','refundable_fee','security_fee']




