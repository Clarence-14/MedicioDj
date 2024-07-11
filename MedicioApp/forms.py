from django import forms
from MedicioApp.models import Appoint

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields = ['name', 'email', 'phone', 'date', 'department', 'doctor', 'message']
