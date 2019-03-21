from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.http import request

from .models import Despesas
from django.forms import ModelForm
import datetime
from django.forms import ModelForm, Select, Textarea, DateInput, TextInput, DecimalField ,ChoiceField



class DespesasForm(ModelForm):
    class Meta:
        model = Despesas
        tipo = forms.CheckboxInput()

        fields = ['descricao', 'created_date', 'valor','categoria','tipo']

        widgets = {
            'descricao': forms.TextInput(),
            'tipo': forms.CheckboxInput(attrs={ 'class':'bootstrap-switch-label','value':'True',  'data-on':"SIM", 'data-off':"NÃO" , 'style':'font-size: 50px;'}),
            'created_date': forms.DateInput(format=( '%Y-%m-%d'), attrs={'class':'date','type':"date" ,'placeholder':'Select a date'}),
        }