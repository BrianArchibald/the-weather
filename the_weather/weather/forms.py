from django.forms import ModelForm, TextInput
from .models import City


class City(ModelForm):
    class Meta:
        model = City
        fields = ['name']
