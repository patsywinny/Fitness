from django import forms
from fitnessapp.models import member, contact


class memberForm(forms.ModelForm):
    class Meta:
        model = member
        fields = '__all__'


class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'