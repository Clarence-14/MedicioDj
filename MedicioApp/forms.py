from django import forms
from MedicioApp.models import Appoint, ImageModel


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image', 'title', 'price']
